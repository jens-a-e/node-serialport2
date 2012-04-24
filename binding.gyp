{
  "targets": [
    {
      "target_name": "serialport2",
      "sources": [
        "src/serialport.cpp",
        "src/serialport_win.cpp",
        "src/serialport_unix.cpp",
        "src/serialport.h"
      ],
      'conditions': [
        ['OS=="win"',
          {
            'sources': [
              'src/win/disphelper.c',
              'src/win/disphelper.h'
            ]
          }
        ]
      ]
    }
  ]
}
