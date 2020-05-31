Downloads geocaches along a GPX route or track.

### Usage

    Settings:
      -i <path>                     Input file path
      -o <path>                     Output file path
      --ge_auth_token <token>       Google Earth geocaching token
      --gspk_auth_token <token>     Groundspeak auth token
      --request_limit <num>         Amount of requests to send [default: 25]
      --search-radius <num>         Radius for search in m [default: 4000]

    Filters:
      --distance <num>              Max distance to trail in m [default: 300]
      --cache_types <arr>           Array of cache types to look for [default: all]
      --container_types <arr>       Array of container types to look for [default: all]
      --difficulty_range <num|num>  Difficulty range to look for [default: all]
      --terrain_range <num|num>     Terrain range to look for [default: all]