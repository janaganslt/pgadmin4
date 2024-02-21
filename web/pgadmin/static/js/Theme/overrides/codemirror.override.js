/////////////////////////////////////////////////////////////
//
// pgAdmin 4 - PostgreSQL Tools
//
// Copyright (C) 2013 - 2023, The pgAdmin Development Team
// This software is released under the PostgreSQL Licence
//
//////////////////////////////////////////////////////////////

export default function cmOverride(theme) {
  const editor = theme.otherVars.editor;
  return {
    '.cm-editor': {
      height: '100%',
      color: editor.fg,
      backgroundColor: editor.bg,

      '&.cm-focused': {
        outline: 'none',

        '& .cm-scroller > .cm-selectionLayer .cm-selectionBackground': {
          background: editor.selectionBg,
        }
      },

      '& .cm-scroller': {
        ...theme.mixins.fontSourceCode,

        '& .cm-content': {
          '&[aria-readonly="true"] + .cm-cursorLayer': {
            display: 'none',
          },

          '& .cm-activeLine': {
            backgroundColor: editor.activeline,
          },

          '& .cm-activeLineManual': {
            backgroundColor: editor.activeline,
          },

          '& .tok-keyword': {
            color: editor.keyword,
            fontWeight: 600
          },
          '& .tok-number': {
            color: editor.number,
            fontWeight: 600
          },
          '& .tok-string': {color: editor.string},
          '& .tok-variable': {color: editor.variable },
          '& .tok-comment': {color: editor.comment},
          '& .tok-operator': { color: editor.operator },
          '& .tok-punctuation': {color: editor.punctuation},
          '& .tok-typeName': {color: editor.type},
        },

        '& .cm-selectionLayer': {
          '& .cm-selectionBackground': {
            background: editor.selectionBg,
          }
        },
      },

      '& .cm-cursorLayer': {
        '& .cm-cursor, & .cm-dropCursor': {
          borderLeftColor: editor.fg,
        }
      },

      '& .cm-gutters': {
        backgroundColor: editor.guttersBg,
        color: editor.guttersFg,
        borderRight: 'none',

        '& .cm-foldGutter': {
          padding: '0px',
          color: editor.fg,
        },

        '& .cm-breakpoint-gutter': {
          padding: '0px 2px',
          cursor: 'pointer',
          '& .cm-gutterElement': {
            fontSize: '1.3em',
            lineHeight: '1.1',
            color: 'red'
          }
        }

      },

      '& .cm-panels-bottom': {
        border: '0 !important',

        '& .cm-search': {
          display: 'none',
        }
      },
      '& .cm-error-highlight': {
        borderBottom: '2px dotted red',
      }
    },
    '.cm-tooltip': {
      backgroundColor: theme.palette.background.default + '!important',
      color: theme.palette.text.primary + '!important',
      border: `1px solid ${theme.otherVars.borderColor} !important`,

      '& li[aria-selected="true"]': {
        backgroundColor: theme.otherVars.treeBgSelected + '!important',
        color: theme.otherVars.treeFgSelected + '!important',
      },

      '& .pg-cm-autocomplete-icon': {
        // marginRight: '2px',
        marginLeft: '-2px',
        padding: '0px 8px',
        backgroundPosition: '50%',
        width: '20px',
        display: 'inline-block',
      },

      '&.pg-autocomp-loader': {
        position: 'absolute',
        paddingRight: '8px',
      }
    }
  };
}
