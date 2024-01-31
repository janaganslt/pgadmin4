{% import 'columns/macros/security.macros' as SECLABEL %}
{% import 'columns/macros/privilege.macros' as PRIVILEGE %}
{% import 'macros/variable.macros' as VARIABLE %}
{% import 'types/macros/get_full_type_sql_format.macros' as GET_TYPE %}
{###  Add column ###}
{% if data.name and  data.cltype %}
ALTER TABLE IF EXISTS {{conn|qtIdent(data.schema, data.table)}}
    ADD COLUMN {{conn|qtIdent(data.name)}} {% if is_sql %}{{data.displaytypname}}{% else %}{{ GET_TYPE.CREATE_TYPE_SQL(conn, data.cltype, data.attlen, data.attprecision, data.hasSqrBracket) }}{% endif %}{% if data.collspcname %}
 COLLATE {{data.collspcname}}{% endif %}{% if data.attnotnull %}
 NOT NULL{% endif %}{% if data.defval is defined and data.defval is not none and data.defval != '' and data.colconstype != 'g' %}
 DEFAULT {{data.defval}}{% endif %}{% if data.colconstype == 'i' %}{% if data.attidentity and data.attidentity == 'a' %} GENERATED ALWAYS AS IDENTITY{% elif data.attidentity and data.attidentity == 'd' %} GENERATED BY DEFAULT AS IDENTITY{% endif %}
{% if data.seqincrement or data.seqcycle or data.seqincrement or data.seqstart or data.seqmin or data.seqmax or data.seqcache %} ( {% endif %}
{% if data.seqcycle is defined and data.seqcycle %}
CYCLE {% endif %}{% if data.seqincrement is defined and data.seqincrement|int(-1) > -1 %}
INCREMENT {{data.seqincrement|int}} {% endif %}{% if data.seqstart is defined and data.seqstart|int(-1) > -1%}
START {{data.seqstart|int}} {% endif %}{% if data.seqmin is defined and data.seqmin|int(-1) > -1%}
MINVALUE {{data.seqmin|int}} {% endif %}{% if data.seqmax is defined and data.seqmax|int(-1) > -1%}
MAXVALUE {{data.seqmax|int}} {% endif %}{% if data.seqcache is defined and data.seqcache|int(-1) > -1%}
CACHE {{data.seqcache|int}} {% endif %}
{% if data.seqincrement or data.seqcycle or data.seqincrement or data.seqstart or data.seqmin or data.seqmax or data.seqcache %}){% endif %}
{% endif %}{% endif %}{% if data.colconstype == 'g' and data.genexpr and data.genexpr != '' %} GENERATED ALWAYS AS ({{data.genexpr}}) STORED{% endif %};

{###  Add comments ###}
{% if data and data.description and data.description != None %}
COMMENT ON COLUMN {{conn|qtIdent(data.schema, data.table, data.name)}}
    IS {{data.description|qtLiteral(conn)}};

{% endif %}
{###  Add variables to column ###}
{% if data.attoptions %}
ALTER TABLE IF EXISTS {{conn|qtIdent(data.schema, data.table)}}
    {{ VARIABLE.SET(conn, 'COLUMN', data.name, data.attoptions) }}

{% endif %}
{###  Alter column statistics value ###}
{% if data.attstattarget is defined and data.attstattarget > -1 %}
ALTER TABLE IF EXISTS {{conn|qtIdent(data.schema, data.table)}}
    ALTER COLUMN {{conn|qtTypeIdent(data.name)}} SET STATISTICS {{data.attstattarget}};

{% endif %}
{###  Alter column storage value ###}
{% if data.attstorage is defined and data.attstorage != data.defaultstorage %}
ALTER TABLE IF EXISTS {{conn|qtIdent(data.schema, data.table)}}
    ALTER COLUMN {{conn|qtTypeIdent(data.name)}} SET STORAGE {%if data.attstorage == 'p' %}
PLAIN{% elif data.attstorage == 'm'%}MAIN{% elif data.attstorage == 'e'%}
EXTERNAL{% elif data.attstorage == 'x'%}EXTENDED{% elif data.attstorage == 'd' %}
DEFAULT{% endif %};

{% endif %}
{###  Alter column compression value ###}
{% if data.attcompression is defined and data.attcompression is not none and data.attcompression != '' %}
ALTER TABLE IF EXISTS {{conn|qtIdent(data.schema, data.table)}}
    ALTER COLUMN {{conn|qtTypeIdent(data.name)}} SET COMPRESSION {{data.attcompression}};

{% endif %}
{###  ACL ###}
{% if data.attacl %}
{% for priv in data.attacl %}
{{ PRIVILEGE.APPLY(conn, data.schema, data.table, data.name, priv.grantee, priv.without_grant, priv.with_grant) }}
{% endfor %}
{% endif %}
{###  Security Lables ###}
{% if data.seclabels %}
{% for r in data.seclabels %}
{{ SECLABEL.APPLY(conn, 'COLUMN',data.schema, data.table, data.name, r.provider, r.label) }}
{% endfor %}
{% endif %}
