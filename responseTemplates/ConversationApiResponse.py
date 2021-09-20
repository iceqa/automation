from trafaret import String, Int, URL, Bool, Or, Date, Float

LIST_CONVERSATION_JSON = {
  "count": Or(Int, Float),
  "page_size": Or(Int, Float),
  "record_index": Or(Int, Float),
  "_links": {
    "self": {
      "href": URL
    }
  },
  "_embedded": {
    "conversations": [
      {
        "uuid": String,
        "name": String,
        "_links": {
          "self": {
            "href": URL
          }
        }
      }
    ]
  }
}

CREATE_CONVERSATION_JSON = {
  "id": String,
  "href": URL
}


UPDATE_CONVERSATION_JSON = {
  "id": String,
  "href": URL
}

GET_CONVERSATION_JSON = {
  "uuid": String,
  "name": String,
  "numbers": {},
  "properties": {
    "video": Bool
  },
  "display_name": String,
  "timestamp": {
    "created": Date,
    "updated": Date,
    "destroyed": Date
  },
  "sequence_number": Int,
  "members": [
    {
      "member_id": String,
      "user_id": String,
      "name": String,
      "state": String,
      "timestamp": {
        "invited": Date,
        "joined": Date,
        "left": Date
      },
      "initiator": {
        "joined": {
          "isSystem": Bool,
          "user_id": String,
          "member_id": String
        }
      },
      "channel": {
        "type": String,
        "leg_id": String,
        "from": {},
        "to": {},
        "leg_ids": [
          {
            "leg_id": String
          }
        ]
      }
    }
  ],
  "api_key": String,
  "_links": {
    "self": {
      "href": URL
    }
  }
}
