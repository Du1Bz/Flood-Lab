> ※ このファイル内の {YOUR_XUID} はご自身のXUIDに置き換えてください。

# Flood Lab - Database Schema & JSON Samples

## Table: `EngineGameVariants`

### Schema
```sql
CREATE TABLE EngineGameVariants (

	ResponseBody TEXT,

	CustomData Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CustomData')) VIRTUAL,

	Tags Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Tags')) VIRTUAL,

	AssetId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetId')) VIRTUAL,

	VersionId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionId')) VIRTUAL,

	PublicName Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublicName')) VIRTUAL,

	Description Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,

	Files Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Files')) VIRTUAL,

	Contributors Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Contributors')) VIRTUAL,

	AssetHome Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetHome')) VIRTUAL,

	AssetStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetStats')) VIRTUAL,

	InspectionResult Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InspectionResult')) VIRTUAL,

	CloneBehavior Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CloneBehavior')) VIRTUAL,

	"Order" Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Order')) VIRTUAL,

	PublishedDate Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublishedDate')) VIRTUAL,

	VersionNumber Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionNumber')) VIRTUAL,

	Admin Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Admin')) VIRTUAL

)
```

**Records: 55**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "CustomData": {
    "SubsetData": {
      "StatBucketGameType": 0,
      "EngineName": "",
      "VariantName": ""
    },
    "LocalizedData": {}
  },
  "Tags": [
    "343i"
  ],
  "AssetId": "1cfee22b-513f-418d-a1d7-2648f1a575e0",
  "VersionId": "a70e2910-88bc-4a98-90b8-e617d6d2c5ae",
  "PublicName": "Slayer",
  "Description": "Control Power Weapons to Eliminate the Enemy.",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/enginegamevariant/1cfee22b-513f-418d-a1d7-2648f1a575e0/a70e2910-88bc-4a98-90b8-e617d6d2c5ae/",
    "FileRelativePaths": [
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_br.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_chs.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_cht.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_de.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_dk.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_en.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_fi.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_fr.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_it.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_jpn.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_kor.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_mx.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_nl.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_no.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_pl.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_pt.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_ru.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_sp.bin",
      "Default.bin",
      "Default.br",
      "Default.chs",
      "Default.cht",
      "Default.de",
      "Default.dk",
      "Default.en",
      "Default.fi",
      "Default.fr",
      "Default.it",
      "Default.jpn",
      "Default.kor",
      "Default.mx",
      "Default.nl",
      "Default.no",
      "Default.pl",
      "Default.pt",
      "Default.ru",
      "Default.sp",
      "Default_guid.txt"
    ],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/enginegamevariant/1cfee22b-513f-418d-a1d7-2648f1a575e0/a70e2910-88bc-4a98-90b8-e617d6d2c5ae/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [],
  "AssetHome": 1,
  "AssetStats": {
    "PlaysRecent": 0,
    "PlaysAllTime": 0,
    "Favorites": 1,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 1078542,
    "AverageRating": 0.0,
    "NumberOfRatings": 0
  },
  "InspectionResult": 50,
  "CloneBehavior": 1,
  "Order": 0,
  "PublishedDate": {
    "ISO8601Date": "2025-07-23T21:41:59.894Z"
  },
  "VersionNumber": 97,
  "Admin": "aaid(5c7909e9-3620-4920-8abf-f18cfb4333b6)",
  "DisplayOwnerOverride": ""
}
  ```

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "CustomData": {
    "SubsetData": {
      "StatBucketGameType": 0,
      "EngineName": "",
      "VariantName": ""
    },
    "LocalizedData": {}
  },
  "Tags": [
    "343i"
  ],
  "AssetId": "9a737720-f83e-4bcc-9c53-6d7f0a8eff6e",
  "VersionId": "ab055133-171b-4237-bd6e-81f8077c8f9b",
  "PublicName": "Slayer-Competitive",
  "Description": "",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/enginegamevariant/9a737720-f83e-4bcc-9c53-6d7f0a8eff6e/ab055133-171b-4237-bd6e-81f8077c8f9b/",
    "FileRelativePaths": [
      "Competitive.bin",
      "Competitive.br",
      "Competitive.chs",
      "Competitive.cht",
      "Competitive.de",
      "Competitive.dk",
      "Competitive.en",
      "Competitive.fi",
      "Competitive.fr",
      "Competitive.it",
      "Competitive.jpn",
      "Competitive.kor",
      "Competitive.mx",
      "Competitive.nl",
      "Competitive.no",
      "Competitive.pl",
      "Competitive.pt",
      "Competitive.ru",
      "Competitive.sp",
      "Competitive_guid.txt",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_br.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_chs.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_cht.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_de.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_dk.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_en.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_fi.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_fr.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_it.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_jpn.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_kor.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_mx.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_nl.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_no.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_pl.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_pt.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_ru.bin",
      "CustomGamesUIMarkup/Slayer_CustomGamesUIMarkup_sp.bin"
    ],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/enginegamevariant/9a737720-f83e-4bcc-9c53-6d7f0a8eff6e/ab055133-171b-4237-bd6e-81f8077c8f9b/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [],
  "AssetHome": 1,
  "AssetStats": {
    "PlaysRecent": 0,
    "PlaysAllTime": 0,
    "Favorites": 1,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 60470,
    "AverageRating": 0.0,
    "NumberOfRatings": 0
  },
  "InspectionResult": 50,
  "CloneBehavior": 1,
  "Order": 0,
  "PublishedDate": {
    "ISO8601Date": "2025-09-04T20:36:20.558Z"
  },
  "VersionNumber": 96,
  "Admin": "aaid(5c7909e9-3620-4920-8abf-f18cfb4333b6)",
  "DisplayOwnerOverride": ""
}
  ```


## Table: `GameVariants`

### Schema
```sql
CREATE TABLE GameVariants (

	ResponseBody TEXT,

	CustomData Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CustomData')) VIRTUAL,

	Tags Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Tags')) VIRTUAL,

	EngineGameVariantLink Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.EngineGameVariantLink')) VIRTUAL,

	AssetId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetId')) VIRTUAL,

	VersionId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionId')) VIRTUAL,

	PublicName Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublicName')) VIRTUAL,

	Description Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,

	Files Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Files')) VIRTUAL,

	Contributors Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Contributors')) VIRTUAL,

	AssetHome Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetHome')) VIRTUAL,

	AssetStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetStats')) VIRTUAL,

	InspectionResult Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InspectionResult')) VIRTUAL,

	CloneBehavior Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CloneBehavior')) VIRTUAL,

	"Order" Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Order')) VIRTUAL,

	PublishedDate Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublishedDate')) VIRTUAL,

	VersionNumber Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionNumber')) VIRTUAL,

	Admin Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Admin')) VIRTUAL

)
```

**Records: 105**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "CustomData": {
    "KeyValues": {
      "globalMalleableProperties.InfiniteAmmo": {
        "uint_value": 1,
        "int_value": 0,
        "double_value": 0.0,
        "string_value": "",
        "wstring_value": "",
        "nothing": false
      },
      "globalMalleableProperties.MotionTrackerEnabled": {
        "uint_value": 1,
        "int_value": 0,
        "double_value": 0.0,
        "string_value": "",
        "wstring_value": "",
        "nothing": false
      },
      "loadoutOptions.Loadout[0].PrimaryWeapon": {
        "uint_value": 0,
        "int_value": 0,
        "double_value": 0.0,
        "string_value": "",
        "wstring_value": "",
        "nothing": false
      },
      "loadoutOptions.Loadout[0].PrimaryWeaponAndConfigurationIdentifier": {
        "uint_value": 11,
        "int_value": 0,
        "double_value": 0.0,
        "string_value": "",
        "wstring_value": "",
        "nothing": false
      },
      "loadoutOptions.Loadout[0].SecondaryWeapon": {
        "uint_value": 16,
        "int_value": 0,
        "double_value": 0.0,
        "string_value": "",
        "wstring_value": "",
        "nothing": false
      },
      "loadoutOptions.Loadout[0].SecondaryWeaponAndConfigurationIdentifier": {
        "uint_value": 20,
        "int_value": 0,
        "double_value": 0.0,
        "string_value": "",
        "wstring_value": "",
        "nothing": false
      },
      "matchFlowOptions.RoundTimeLimit": {
        "uint_value": 11,
        "int_value": 0,
        "double_value": 0.0,
        "string_value": "",
        "wstring_value": "",
        "nothing": false
      },
      "matchFlowOptions.ScoreToWinRound": {
        "uint_value": 24,
        "int_value": 0,
        "double_value": 0.0,
        "string_value": "",
        "wstring_value": "",
        "nothing": false
      },
      "respawnOptions.MinimumRespawnTimeInSeconds": {
        "uint_value": 1,
        "int_value": 0,
        "double_value": 0.0,
        "string_value": "",
        "wstring_value": "",
        "nothing": false
      }
    },
    "HasNodeGraph": false
  },
  "Tags": [
    "Arena",
    "Slayer",
    "1v1",
    "BRT",
    "Training"
  ],
  "EngineGameVariantLink": {
    "AssetId": "1cfee22b-513f-418d-a1d7-2648f1a575e0",
    "VersionId": "a70e2910-88bc-4a98-90b8-e617d6d2c5ae",
    "PublicName": "Slayer",
    "Description": "Control Power Weapons to Eliminate the Enemy.",
    "Files": {
      "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/enginegamevariant/1cfee22b-513f-418d-a1d7-2648f1a575e0/a70e2910-88bc-4a98-90b8-e617d6d2c5ae/",
      "FileRelativePaths": [],
      "PrefixEndpoint": {
        "AuthorityId": "iUgcFiles",
        "Path": "/ugcstorage/enginegamevariant/1cfee22b-513f-418d-a1d7-2648f1a575e0/a70e2910-88bc-4a98-90b8-e617d6d2c5ae/",
        "QueryString": null,
        "RetryPolicyId": "linearretry",
        "TopicName": "",
        "AcknowledgementTypeId": 0,
        "AuthenticationLifetimeExtensionSupported": false,
        "ClearanceAware": false
      }
    },
    "Contributors": [],
    "AssetHome": 1,
    "AssetStats": {
      "PlaysRecent": 0,
      "PlaysAllTime": 0,
      "Favorites": 1,
      "Likes": 0,
      "Bookmarks": 0,
      "ParentAssetCount": 1078542,
      "AverageRating": 0.0,
      "NumberOfRatings": 0
    },
    "InspectionResult": 50,
    "CloneBehavior": 1,
    "Order": 0,
    "PublishedDate": {
      "ISO8601Date": "2025-07-23T21:41:59.894Z"
    },
    "VersionNumber": 97,
    "Admin": "aaid(5c7909e9-3620-4920-8abf-f18cfb4333b6)",
    "DisplayOwnerOverride": ""
  },
  "AssetId": "fa4dc960-5240-4aaa-8486-eb6bc0aa95aa",
  "VersionId": "628d8504-fc36-4b08-8743-8d7433e867a4",
  "PublicName": "BRT",
  "Description": "1v1 BR Training",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/ugcgamevariant/fa4dc960-5240-4aaa-8486-eb6bc0aa95aa/628d8504-fc36-4b08-8743-8d7433e867a4/",
    "FileRelativePaths": [
      "images/hero.png",
      "images/screenshot1.Png",
      "images/screenshot1.png",
      "images/thumbnail.png"
    ],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/ugcgamevariant/fa4dc960-5240-4aaa-8486-eb6bc0aa95aa/628d8504-fc36-4b08-8743-8d7433e867a4/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [
    "xuid({YOUR_XUID})"
  ],
  "AssetHome": 2,
  "AssetStats": {
    "PlaysRecent": 19,
    "PlaysAllTime": 19467,
    "Favorites": 208,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 0,
    "AverageRating": 4.666666666666667,
    "NumberOfRatings": 12
  },
  "InspectionResult": 0,
  "CloneBehavior": 0,
  "Order": 0,
  "PublishedDate": {
    "ISO8601Date": "2026-04-23T08:46:22.695Z"
  },
  "VersionNumber": 3,
  "Admin": "xuid({YOUR_XUID})",
  "DisplayOwnerOverride": ""
}
  ```

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "CustomData": {
    "KeyValues": {},
    "HasNodeGraph": false
  },
  "Tags": [
    "343i",
    "Ranked",
    "Slayer"
  ],
  "EngineGameVariantLink": {
    "AssetId": "9a737720-f83e-4bcc-9c53-6d7f0a8eff6e",
    "VersionId": "ab055133-171b-4237-bd6e-81f8077c8f9b",
    "PublicName": "Slayer-Competitive",
    "Description": "",
    "Files": {
      "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/enginegamevariant/9a737720-f83e-4bcc-9c53-6d7f0a8eff6e/ab055133-171b-4237-bd6e-81f8077c8f9b/",
      "FileRelativePaths": [],
      "PrefixEndpoint": {
        "AuthorityId": "iUgcFiles",
        "Path": "/ugcstorage/enginegamevariant/9a737720-f83e-4bcc-9c53-6d7f0a8eff6e/ab055133-171b-4237-bd6e-81f8077c8f9b/",
        "QueryString": null,
        "RetryPolicyId": "linearretry",
        "TopicName": "",
        "AcknowledgementTypeId": 0,
        "AuthenticationLifetimeExtensionSupported": false,
        "ClearanceAware": false
      }
    },
    "Contributors": [],
    "AssetHome": 1,
    "AssetStats": {
      "PlaysRecent": 0,
      "PlaysAllTime": 0,
      "Favorites": 1,
      "Likes": 0,
      "Bookmarks": 0,
      "ParentAssetCount": 60470,
      "AverageRating": 0.0,
      "NumberOfRatings": 0
    },
    "InspectionResult": 50,
    "CloneBehavior": 1,
    "Order": 0,
    "PublishedDate": {
      "ISO8601Date": "2025-09-04T20:36:20.558Z"
    },
    "VersionNumber": 96,
    "Admin": "aaid(5c7909e9-3620-4920-8abf-f18cfb4333b6)",
    "DisplayOwnerOverride": ""
  },
  "AssetId": "c2d20d44-8606-4669-b894-afae15b3524f",
  "VersionId": "0091d411-f90d-44a7-aac3-ccc7ff2b131f",
  "PublicName": "Ranked:Slayer",
  "Description": "Bandit Evo loadouts, Friendly-Fire enabled, Motion Tracker disabled. Slay the enemy team.",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/ugcgamevariant/c2d20d44-8606-4669-b894-afae15b3524f/0091d411-f90d-44a7-aac3-ccc7ff2b131f/",
    "FileRelativePaths": [
      "images/hero.png",
      "images/screenshot1.Png",
      "images/screenshot1.png",
      "images/screenshot2.Png",
      "images/screenshot2.png",
      "images/screenshot3.Png",
      "images/screenshot3.png",
      "images/thumbnail.png"
    ],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/ugcgamevariant/c2d20d44-8606-4669-b894-afae15b3524f/0091d411-f90d-44a7-aac3-ccc7ff2b131f/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [],
  "AssetHome": 1,
  "AssetStats": {
    "PlaysRecent": 40923,
    "PlaysAllTime": 38606846,
    "Favorites": 52971,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 145,
    "AverageRating": 3.822296280369813,
    "NumberOfRatings": 27906
  },
  "InspectionResult": 0,
  "CloneBehavior": 0,
  "Order": 0,
  "PublishedDate": {
    "ISO8601Date": "2021-11-15T12:00:00Z"
  },
  "VersionNumber": 8,
  "Admin": "aaid(5c7909e9-3620-4920-8abf-f18cfb4333b6)",
  "DisplayOwnerOverride": ""
}
  ```


## Table: `InventoryItems`

### Schema
```sql
CREATE TABLE InventoryItems (

	ResponseBody TEXT,

	Path TEXT,

	LastUpdated DATETIME,

	Id Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CommonData.Id')) VIRTUAL,

	Quality Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CommonData.Quality')) VIRTUAL

)
```

**Records: 1007**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "TagId": -1975245852,
  "MeshIndex": -1,
  "CommonData": {
    "Id": "4241927-011-olympus",
    "HideUntilOwned": false,
    "Title": {
      "status": "Ready",
      "value": "Artificer Vambrace",
      "translations": {
        "qps-ploc": "Ąŗтïƒїċèг Vªмвѓªсē !!! !!",
        "qps-ploca": "Äґţіƒΐςĕř Vαmъґāсз !!! !!",
        "qps-plocm": "Аŗτїƒιçęŗ Vàmьŗâċę !!! !!"
      }
    },
    "Description": {
      "status": "Ready",
      "value": "Every motion serves a greater purpose, which the sensors in these attachments ensure is not forgotten or overlooked.",
      "translations": {
        "qps-ploc": "Зνέяў мοťïöη śĕřνéś ă ĝřëдŧéг φųřрόšé, ŵђϊçĥ τне śėпѕθяŝ įή ťћєšè äтťāčћmĕⁿŧŝ ěиşųřз ĩś πбт ƒθŗğоţтеи ôŗ бνєřŀбоκёð. !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !",
        "qps-ploca": "Ενέгу mòţіοŋ ŝέяνèѕ â ģгėǻŧёґ рμгρσŝė, ŵђï¢ђ тђĕ şέпśσґѕ īи ŧħěşз дтŧα¢ħмêňţŝ ěпşúŗë іŝ ηöт ƒōŕĝòŧтзπ оř óνėѓĺǿοќęđ. !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !",
        "qps-plocm": "Єνėѓў мõţϊόŋ śéяνėş ā ģґёąťєŕ рüřφŏś℮, шћϊςĥ ŧђε ŝĕлśθґś ĭņ тĥēŝё âţŧăĉћмзйťş éňşΰѓë їѕ пøŧ ƒóřğόττëπ θѓ όνέяŀóóќęð. !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !!! !"
      }
    },
    "FeatureFlag": true,
    "ItemAvailability": {
      "status": "Test",
      "value": ""
    },
    "DateReleased": {
      "ISO8601Date": ""
    },
    "AltName": {
      "status": "Test",
      "value": "4241927-ArmorWristAttachment-Mark-VII",
      "translations": {
        "qps-ploc": "4241927-ÁřmοŗẄѓìşťΆŧţαċћмέпţ-Мãŗķ-VÎІ !!! !!! !!! !!",
        "qps-ploca": "4241927-ÄŕмőŗẀřϊşτÃтťªçђméňт-Μåѓќ-VΪΊ !!! !!! !!! !!",
        "qps-plocm": "4241927-ĂŕмθřШŗïѕţΔţŧăςђмèήŧ-Μăѓќ-VĮĮ !!! !!! !!! !!"
      }
    },
    "IconStringId": {
      "m_identifier": -1
    },
    "SpriteBitmap": 0,
    "SpriteFrameIndex": 0,
    "AltSpriteBitmap": 0,
    "AltSpriteFrameIndex": 0,
    "DisplayPath": {
      "Width": 150,
      "Height": 150,
      "Media": {
        "MediaUrl": {
          "AuthorityId": "",
          "Path": "progression/Inventory/Armor/WristAttachments/4241927-ArmorWristAttachment-Mark-VII-SM.png",
          "RetryPolicyId": "",
          "TopicName": "",
          "AcknowledgementTypeId": "NoAcknowledgement",
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        },
        "MimeType": "image/png",
        "Caption": {
          "status": "Test",
          "value": ""
        },
        "AlternateText": {
          "status": "Test",
          "value": ""
        },
        "FolderPath": "progression/Inventory/Armor/WristAttachments",
        "FileName": "4241927-ArmorWristAttachment-Mark-VII-SM.png"
      }
    },
    "Quality": "Epic",
    "ManufacturerId": 9,
    "Type": "ArmorWristAttachment",
    "RewardTrack": "",
    "ParentPaths": [
      {
        "Path": "Inventory/Armor/Themes/007-001-olympus-c13d0b38.json",
        "Type": "ArmorTheme"
      }
    ],
    "SortingMetadata": {
      "categoryWeight": 0,
      "subCategoryWeight": 0
    },
    "SeasonNumber": 13001,
    "OriginalSeasonNumber": 13001,
    "IsCrossCompatible": false
  }
}
  ```
- **Path**: `Inventory/armor/wristattachments/4241927-ArmorWristAttachment-Mark-VII.json`
- **LastUpdated**: `2026-05-11T22:10:49.101+09:00`

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "TagId": 0,
  "ThemeName": {
    "m_identifier": -862015688
  },
  "EmblemShaderName": {
    "m_identifier": -1
  },
  "AvailableConfigurations": [
    {
      "ConfigurationId": -1788399426,
      "ConfigurationPath": "Configuration/Emblems/Coatings/1000-000-ecdc1bcd.json"
    },
    {
      "ConfigurationId": 1540133627,
      "ConfigurationPath": "Configuration/Emblems/Coatings/1000-000-cf1c5706.json"
    },
    {
      "ConfigurationId": -1698878342,
      "ConfigurationPath": "Configuration/Emblems/Coatings/1000-000-8a3325cd.json"
    },
    {
      "ConfigurationId": 176812955,
      "ConfigurationPath": "Configuration/Emblems/Coatings/1000-000-cabc2933.json"
    },
    {
      "ConfigurationId": -1735535024,
      "ConfigurationPath": "Configuration/Emblems/Coatings/1000-000-3f8ab8f6.json"
    },
    {
      "ConfigurationId": 1834538618,
      "ConfigurationPath": "Configuration/Emblems/Coatings/1000-000-7d7b75d9.json"
    },
    {
      "ConfigurationId": -411885605,
      "ConfigurationPath": "Configuration/Emblems/Coatings/1000-000-485b05b7.json"
    },
    {
      "ConfigurationId": 824330229,
      "ConfigurationPath": "Configuration/Emblems/Coatings/1000-000-227adf2f.json"
    }
  ],
  "CommonData": {
    "Id": "104-001-popculture-de-8643a9b3",
    "HideUntilOwned": false,
    "Title": {
      "status": "Ready",
      "value": "Seeker",
      "translations": {
        "cs-CZ": "Hledač",
        "da-DK": "Søger",
        "de-DE": "Sucher",
        "el-GR": "Αναζητητής",
        "es-ES": "Buscador",
        "es-MX": "Buscador",
        "fi-FI": "Etsijä",
        "fr-FR": "Traqueur",
        "hu-HU": "Kereső",
        "it-IT": "Seeker",
        "ja-JP": "シーカー",
        "ko-KR": "시커",
        "nb-NO": "Søker",
        "nl-NL": "Zoeker",
        "pl-PL": "Szperacz",
        "pt-BR": "Caçador",
        "pt-PT": "Seeker",
        "ru-RU": "Искатель",
        "sv-SE": "Sökare",
        "tr-TR": "Arayıcı",
        "zh-CN": "探测者",
        "zh-TW": "搜索者",
        "qps-ploc": "Śĕėкêя !",
        "qps-ploca": "Śěėķεŕ !",
        "qps-plocm": "Śêěκёř !"
      }
    },
    "Description": {
      "status": "Ready",
      "value": "You rejected perfection.",
      "translations": {
        "cs-CZ": "Odmítli jste dokonalost.",
        "da-DK": "Du afviste perfektion.",
        "de-DE": "Du hast Perfektion verschmäht.",
        "el-GR": "Απέρριψες την τελειότητα.",
        "es-ES": "Has rechazado la perfección.",
        "es-MX": "Rechazaste la perfección.",
        "fi-FI": "Torjuit täydellisyyden.",
        "fr-FR": "Vous avez refusé la perfection.",
        "hu-HU": "Elutasítottad a tökéletest.",
        "it-IT": "Hai rifiutato la perfezione.",
        "ja-JP": "君は完璧であることを拒んだ。",
        "ko-KR": "당신은 완벽을 거부했습니다.",
        "nb-NO": "Du ga avkall på perfeksjon.",
        "nl-NL": "Je hebt perfectie afgewezen.",
        "pl-PL": "Odrzuciłeś doskonałość.",
        "pt-BR": "Você rejeitou a perfeição.",
        "pt-PT": "Rejeitaste a perfeição.",
        "ru-RU": "Ты отвергаешь совершенство.",
        "sv-SE": "Du frånsade dig perfektion.",
        "tr-TR": "Mükemmelliği reddettin.",
        "zh-CN": "你拒绝了完美。",
        "zh-TW": "你拒絕了完美。",
        "qps-ploc": "Ŷōü язĵэčт℮δ φ℮ŕƒĕ¢τïσň. !!! !!! !",
        "qps-ploca": "Ýǿύ гёј℮¢ťěđ ρ℮ґƒеčţíõл. !!! !!! !",
        "qps-plocm": "Ўóů яèјĕςŧεđ φеѓƒё¢ţιοп. !!! !!! !"
      }
    },
    "FeatureFlag": true,
    "ItemAvailability": {
      "status": "Test",
      "value": "",
      "translations": {}
    },
    "DateReleased": {
      "ISO8601Date": ""
    },
    "AltName": {
      "status": "Test",
      "value": "104-001-popculture-de-8643a9b3",
      "translations": {
        "qps-ploc": "104-001-рŏрċύℓŧΰѓэ-đ℮-8643ă9в3 !!! !!! !!!",
        "qps-ploca": "104-001-ροрĉűŀŧůŕэ-đė-8643ά9в3 !!! !!! !!!",
        "qps-plocm": "104-001-рöφćцłŧųѓє-đё-8643ą9ъ3 !!! !!! !!!"
      }
    },
    "IconStringId": {
      "m_identifier": -1
    },
    "SpriteBitmap": 0,
    "SpriteFrameIndex": 0,
    "AltSpriteBitmap": 0,
    "AltSpriteFrameIndex": 0,
    "DisplayPath": {
      "Width": 358,
      "Height": 358,
      "Media": {
        "MediaUrl": {
          "AuthorityId": "",
          "Path": "progression/Inventory/Emblems/popculture_dealerschoice_seeker_emblem.png",
          "RetryPolicyId": "",
          "TopicName": "",
          "AcknowledgementTypeId": "NoAcknowledgement",
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        },
        "MimeType": "",
        "Caption": {
          "status": "Test",
          "value": "",
          "translations": {}
        },
        "AlternateText": {
          "status": "Test",
          "value": "",
          "translations": {}
        },
        "FolderPath": "",
        "FileName": ""
      },
      "MimeType": "image/png",
      "FolderPath": "progression/Inventory/Emblems",
      "FileName": "popculture_dealerschoice_seeker_emblem.png"
    },
    "Quality": "Epic",
    "ManufacturerId": 8,
    "Type": "SpartanEmblem",
    "RewardTrack": "",
    "ParentPaths": [],
    "SortingMetadata": {
      "categoryWeight": 0,
      "subCategoryWeight": 0
    },
    "SeasonNumber": 13001,
    "OriginalSeasonNumber": 13001,
    "IsCrossCompatible": true,
    "Season": {
      "status": "Test",
      "value": "",
      "translations": {}
    }
  }
}
  ```
- **Path**: `Inventory/spartan/emblems/104-001-popculture-de-8643a9b3.json`
- **LastUpdated**: `2026-05-11T22:10:49.629+09:00`


## Table: `Maps`

### Schema
```sql
CREATE TABLE Maps (

	ResponseBody TEXT,

	CustomData Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CustomData')) VIRTUAL,

	Tags Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Tags')) VIRTUAL,

	PrefabLinks Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PrefabLinks')) VIRTUAL,

	AssetId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetId')) VIRTUAL,

	VersionId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionId')) VIRTUAL,

	PublicName Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublicName')) VIRTUAL,

	Description Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,

	Files Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Files')) VIRTUAL,

	Contributors Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Contributors')) VIRTUAL,

	AssetHome Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetHome')) VIRTUAL,

	AssetStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetStats')) VIRTUAL,

	InspectionResult Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InspectionResult')) VIRTUAL,

	CloneBehavior Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CloneBehavior')) VIRTUAL,

	"Order" Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Order')) VIRTUAL,

	PublishedDate Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublishedDate')) VIRTUAL,

	VersionNumber Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionNumber')) VIRTUAL,

	Admin Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Admin')) VIRTUAL

)
```

**Records: 246**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "CustomData": {
    "NumOfObjectsOnMap": 5093,
    "TagLevelId": 992358984,
    "IsBaked": false,
    "HasNodeGraph": false
  },
  "Tags": [],
  "PrefabLinks": [],
  "AssetId": "1a6cfc2e-ec86-48e1-9464-1ce1bff6ed48",
  "VersionId": "3a382104-9b89-4e6e-aa18-0affaa98f478",
  "PublicName": "Lattice - Ranked",
  "Description": "This abandoned hydroelectric facility holds secrets once buried under the ice.",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/map/1a6cfc2e-ec86-48e1-9464-1ce1bff6ed48/3a382104-9b89-4e6e-aa18-0affaa98f478/",
    "FileRelativePaths": [
      "audioocclusion.blob",
      "fo13_frost.mvar",
      "images/hero.jpg",
      "images/screenshot1.jpg",
      "images/screenshot2.jpg",
      "images/screenshot3.jpg",
      "images/thumbnail.jpg",
      "lightprobes.blob",
      "map.mvar",
      "navmesh.blob"
    ],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/map/1a6cfc2e-ec86-48e1-9464-1ce1bff6ed48/3a382104-9b89-4e6e-aa18-0affaa98f478/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [
    "xuid(2814640426484785)",
    "xuid(2814673621658978)",
    "xuid(2814620018427310)"
  ],
  "AssetHome": 1,
  "AssetStats": {
    "PlaysRecent": 10524,
    "PlaysAllTime": 620420,
    "Favorites": 5009,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 17,
    "AverageRating": 3.393939393939394,
    "NumberOfRatings": 165
  },
  "InspectionResult": 0,
  "CloneBehavior": 0,
  "Order": 0,
  "PublishedDate": {
    "ISO8601Date": "2021-11-15T12:00:00Z"
  },
  "VersionNumber": 4,
  "Admin": "xuid(2814673621658978)",
  "DisplayOwnerOverride": ""
}
  ```

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "CustomData": {
    "NumOfObjectsOnMap": 4743,
    "TagLevelId": 992358984,
    "IsBaked": false,
    "HasNodeGraph": true
  },
  "Tags": [],
  "PrefabLinks": [],
  "AssetId": "654dff62-d618-496a-8914-06ab73d991e3",
  "VersionId": "87e7bd29-9914-48f3-81e0-38ad200e1e4e",
  "PublicName": "Interference",
  "Description": "Reimagination of the Halo 5's map The Rig with a snowy theme. Upscaled to accommodate Infinite's mechanics. It supports: Slayer, Strongholds and King of the Hill.",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/map/654dff62-d618-496a-8914-06ab73d991e3/87e7bd29-9914-48f3-81e0-38ad200e1e4e/",
    "FileRelativePaths": [
      "audioocclusion.blob",
      "fo13_frost.mvar",
      "images/hero.jpg",
      "images/screenshot1.jpg",
      "images/screenshot2.jpg",
      "images/screenshot3.jpg",
      "images/thumbnail.jpg",
      "lightprobes.blob",
      "map.mvar",
      "navmesh.blob"
    ],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/map/654dff62-d618-496a-8914-06ab73d991e3/87e7bd29-9914-48f3-81e0-38ad200e1e4e/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [
    "xuid(2814673621658978)",
    "xuid(2533274885566464)",
    "xuid(2535434382229776)",
    "xuid(2535431248047890)",
    "xuid(2533274888129123)",
    "xuid(2535409849610595)",
    "xuid(2533274798663195)",
    "xuid(2533274955934650)",
    "xuid(2659938529929265)"
  ],
  "AssetHome": 1,
  "AssetStats": {
    "PlaysRecent": 3670,
    "PlaysAllTime": 3645172,
    "Favorites": 4503,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 20,
    "AverageRating": 3.902350813743219,
    "NumberOfRatings": 553
  },
  "InspectionResult": 0,
  "CloneBehavior": 2,
  "Order": 0,
  "PublishedDate": {
    "ISO8601Date": "2021-11-15T12:00:00Z"
  },
  "VersionNumber": 5,
  "Admin": "xuid(2533274885566464)",
  "DisplayOwnerOverride": "xuid(2533274885566464)"
}
  ```


## Table: `MatchStats`

### Schema
```sql
CREATE TABLE MatchStats (

   ResponseBody TEXT,

   MatchId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.MatchId')) VIRTUAL,

   MatchInfo Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.MatchInfo')) VIRTUAL,

   Teams Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Teams')) VIRTUAL,

   Players Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Players')) VIRTUAL

)
```

**Records: 3366**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "MatchId": "86c0de94-b42f-4926-ac40-19c39d3b0284",
  "MatchInfo": {
    "StartTime": "2026-05-06T14:58:55.16Z",
    "EndTime": "2026-05-06T15:03:38.261Z",
    "Duration": "PT4M43.0870026S",
    "LifecycleMode": 1,
    "GameVariantCategory": 6,
    "LevelId": "c7b7baf0-f206-11e4-ae9a-24be05e24f7e",
    "MapVariant": {
      "AssetKind": 2,
      "AssetId": "29c99861-84c6-4402-ba09-7ab4b442bf04",
      "VersionId": "28f9dd56-ce15-418b-ac96-e35461646a03"
    },
    "UgcGameVariant": {
      "AssetKind": 6,
      "AssetId": "fa4dc960-5240-4aaa-8486-eb6bc0aa95aa",
      "VersionId": "628d8504-fc36-4b08-8743-8d7433e867a4"
    },
    "ClearanceId": "d22ce0c2-d635-43e7-8d7f-4506a43b20f3",
    "Playlist": null,
    "PlaylistExperience": null,
    "PlaylistMapModePair": null,
    "SeasonId": null,
    "PlayableDuration": "PT4M43.094S",
    "TeamsEnabled": true,
    "TeamScoringEnabled": true,
    "GameplayInteraction": 1
  },
  "Teams": [
    {
      "TeamId": 0,
      "Outcome": 3,
      "Rank": 2,
      "Stats": {
        "CoreStats": {
          "Score": 12,
          "PersonalScore": 1200,
          "RoundsWon": 0,
          "RoundsLost": 1,
          "RoundsTied": 0,
          "Kills": 12,
          "Deaths": 25,
          "Assists": 0,
          "KDA": -13.0,
          "Suicides": 0,
          "Betrayals": 0,
          "AverageLifeDuration": "PT9.5S",
          "GrenadeKills": 1,
          "HeadshotKills": 11,
          "MeleeKills": 0,
          "PowerWeaponKills": 4,
          "ShotsFired": 145,
          "ShotsHit": 67,
          "Accuracy": 46.2,
          "DamageDealt": 4167,
          "DamageTaken": 5878,
          "CalloutAssists": 0,
          "VehicleDestroys": 0,
          "DriverAssists": 0,
          "Hijacks": 0,
          "EmpAssists": 0,
          "MaxKillingSpree": 3,
          "Medals": [
            {
              "NameId": 4229934157,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 622331684,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2123530881,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 1512363953,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 3233952928,
              "Count": 2,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2602963073,
              "Count": 3,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2852571933,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            }
          ],
          "PersonalScores": [
            {
              "NameId": 1024030246,
              "Count": 12,
              "TotalPersonalScoreAwarded": 1200
            }
          ],
          "DeprecatedDamageDealt": 4167.0,
          "DeprecatedDamageTaken": 5878.0,
          "Spawns": 25,
          "ObjectivesCompleted": 0
        },
        "PvpStats": {
          "Kills": 12,
          "Deaths": 25,
          "Assists": 0,
          "KDA": -13.0
        }
      }
    },
    {
      "TeamId": 1,
      "Outcome": 2,
      "Rank": 1,
      "Stats": {
        "CoreStats": {
          "Score": 25,
          "PersonalScore": 2500,
          "RoundsWon": 1,
          "RoundsLost": 0,
          "RoundsTied": 0,
          "Kills": 25,
          "Deaths": 12,
          "Assists": 0,
          "KDA": 13.0,
          "Suicides": 0,
          "Betrayals": 0,
          "AverageLifeDuration": "PT19.2S",
          "GrenadeKills": 3,
          "HeadshotKills": 17,
          "MeleeKills": 2,
          "PowerWeaponKills": 3,
          "ShotsFired": 160,
          "ShotsHit": 91,
          "Accuracy": 56.87,
          "DamageDealt": 5878,
          "DamageTaken": 4167,
          "CalloutAssists": 0,
          "VehicleDestroys": 0,
          "DriverAssists": 0,
          "Hijacks": 0,
          "EmpAssists": 0,
          "MaxKillingSpree": 6,
          "Medals": [
            {
              "NameId": 2852571933,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2780740615,
              "Count": 2,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2602963073,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2123530881,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 3655682764,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 622331684,
              "Count": 2,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 4229934157,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2063152177,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 1477806194,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 1169390319,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            }
          ],
          "PersonalScores": [
            {
              "NameId": 1024030246,
              "Count": 25,
              "TotalPersonalScoreAwarded": 2500
            }
          ],
          "DeprecatedDamageDealt": 5878.0,
          "DeprecatedDamageTaken": 4167.0,
          "Spawns": 13,
          "ObjectivesCompleted": 0
        },
        "PvpStats": {
          "Kills": 25,
          "Deaths": 12,
          "Assists": 0,
          "KDA": 13.0
        }
      }
    }
  ],
  "Players": [
    {
      "PlayerId": "xuid({YOUR_XUID})",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 0,
      "Outcome": 3,
      "Rank": 2,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-06T14:58:55.161Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT4M43.094S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 0,
          "Stats": {
            "CoreStats": {
              "Score": 12,
              "PersonalScore": 1200,
              "RoundsWon": 0,
              "RoundsLost": 1,
              "RoundsTied": 0,
              "Kills": 12,
              "Deaths": 25,
              "Assists": 0,
              "KDA": -13.0,
              "Suicides": 0,
              "Betrayals": 0,
              "AverageLifeDuration": "PT9.5S",
              "GrenadeKills": 1,
              "HeadshotKills": 11,
              "MeleeKills": 0,
              "PowerWeaponKills": 4,
              "ShotsFired": 145,
              "ShotsHit": 67,
              "Accuracy": 46.2,
              "DamageDealt": 4167,
              "DamageTaken": 5878,
              "CalloutAssists": 0,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 3,
              "Medals": [
                {
                  "NameId": 4229934157,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 622331684,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2123530881,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 1512363953,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 3233952928,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2602963073,
                  "Count": 3,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 1024030246,
                  "Count": 12,
                  "TotalPersonalScoreAwarded": 1200
                }
              ],
              "DeprecatedDamageDealt": 4167.0,
              "DeprecatedDamageTaken": 5878.0,
              "Spawns": 25,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 12,
              "Deaths": 25,
              "Assists": 0,
              "KDA": -13.0
            }
          }
        }
      ]
    },
    {
      "PlayerId": "xuid(2533274962782816)",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 1,
      "Outcome": 2,
      "Rank": 1,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-06T14:58:55.173Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT4M43.094S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 1,
          "Stats": {
            "CoreStats": {
              "Score": 25,
              "PersonalScore": 2500,
              "RoundsWon": 1,
              "RoundsLost": 0,
              "RoundsTied": 0,
              "Kills": 25,
              "Deaths": 12,
              "Assists": 0,
              "KDA": 13.0,
              "Suicides": 0,
              "Betrayals": 0,
              "AverageLifeDuration": "PT19.2S",
              "GrenadeKills": 3,
              "HeadshotKills": 17,
              "MeleeKills": 2,
              "PowerWeaponKills": 3,
              "ShotsFired": 160,
              "ShotsHit": 91,
              "Accuracy": 56.87,
              "DamageDealt": 5878,
              "DamageTaken": 4167,
              "CalloutAssists": 0,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 6,
              "Medals": [
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2780740615,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2602963073,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2123530881,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 3655682764,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 622331684,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 4229934157,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2063152177,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 1477806194,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 1169390319,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 1024030246,
                  "Count": 25,
                  "TotalPersonalScoreAwarded": 2500
                }
              ],
              "DeprecatedDamageDealt": 5878.0,
              "DeprecatedDamageTaken": 4167.0,
              "Spawns": 13,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 25,
              "Deaths": 12,
              "Assists": 0,
              "KDA": 13.0
            }
          }
        }
      ]
    }
  ]
}
  ```

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "MatchId": "90e0b3e4-b72f-48ce-9198-43c89f6814ef",
  "MatchInfo": {
    "StartTime": "2026-05-05T12:51:02.361Z",
    "EndTime": "2026-05-05T13:01:45.601Z",
    "Duration": "PT9M49.4544317S",
    "LifecycleMode": 3,
    "GameVariantCategory": 6,
    "LevelId": "67490e04-926c-4e7c-a764-071f26e0c24c",
    "MapVariant": {
      "AssetKind": 2,
      "AssetId": "654dff62-d618-496a-8914-06ab73d991e3",
      "VersionId": "87e7bd29-9914-48f3-81e0-38ad200e1e4e"
    },
    "UgcGameVariant": {
      "AssetKind": 6,
      "AssetId": "c2d20d44-8606-4669-b894-afae15b3524f",
      "VersionId": "0091d411-f90d-44a7-aac3-ccc7ff2b131f"
    },
    "ClearanceId": "d121af91-a1bc-4f5d-b2c6-36b08808b1ba",
    "Playlist": {
      "AssetKind": 3,
      "AssetId": "dcb2e24e-05fb-4390-8076-32a0cdb4326e",
      "VersionId": "1f86eb44-cf6d-4969-950c-bebc8ce04407"
    },
    "PlaylistExperience": 2,
    "PlaylistMapModePair": {
      "AssetKind": 7,
      "AssetId": "6d60d1d2-cc97-4b4e-88a4-9755e110e3c3",
      "VersionId": "b0440694-46e4-4981-9431-bdf8b00e948e"
    },
    "SeasonId": "Csr/Seasons/CsrSeason13-2.json",
    "PlayableDuration": "PT9M49.453S",
    "TeamsEnabled": true,
    "TeamScoringEnabled": true,
    "GameplayInteraction": 1
  },
  "Teams": [
    {
      "TeamId": 0,
      "Outcome": 3,
      "Rank": 2,
      "Stats": {
        "CoreStats": {
          "Score": 47,
          "PersonalScore": 5810,
          "RoundsWon": 0,
          "RoundsLost": 1,
          "RoundsTied": 0,
          "Kills": 47,
          "Deaths": 52,
          "Assists": 20,
          "KDA": 1.66,
          "Suicides": 0,
          "Betrayals": 0,
          "AverageLifeDuration": "PT34.9S",
          "GrenadeKills": 4,
          "HeadshotKills": 29,
          "MeleeKills": 7,
          "PowerWeaponKills": 5,
          "ShotsFired": 704,
          "ShotsHit": 364,
          "Accuracy": 51.7,
          "DamageDealt": 16750,
          "DamageTaken": 17846,
          "CalloutAssists": 6,
          "VehicleDestroys": 0,
          "DriverAssists": 0,
          "Hijacks": 0,
          "EmpAssists": 0,
          "MaxKillingSpree": 4,
          "Medals": [
            {
              "NameId": 1512363953,
              "Count": 3,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 4229934157,
              "Count": 3,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 548533137,
              "Count": 2,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 3334154676,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 1169571763,
              "Count": 3,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2852571933,
              "Count": 4,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 622331684,
              "Count": 4,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2414983178,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2602963073,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 4277328263,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            }
          ],
          "PersonalScores": [
            {
              "NameId": 638246808,
              "Count": 21,
              "TotalPersonalScoreAwarded": 1050
            },
            {
              "NameId": 1024030246,
              "Count": 47,
              "TotalPersonalScoreAwarded": 4700
            },
            {
              "NameId": 152718958,
              "Count": 6,
              "TotalPersonalScoreAwarded": 60
            }
          ],
          "DeprecatedDamageDealt": 16750.0,
          "DeprecatedDamageTaken": 17846.0,
          "Spawns": 54,
          "ObjectivesCompleted": 0
        },
        "PvpStats": {
          "Kills": 47,
          "Deaths": 52,
          "Assists": 20,
          "KDA": 1.66
        }
      }
    },
    {
      "TeamId": 1,
      "Outcome": 2,
      "Rank": 1,
      "Stats": {
        "CoreStats": {
          "Score": 50,
          "PersonalScore": 6160,
          "RoundsWon": 1,
          "RoundsLost": 0,
          "RoundsTied": 0,
          "Kills": 52,
          "Deaths": 49,
          "Assists": 22,
          "KDA": 10.33,
          "Suicides": 1,
          "Betrayals": 1,
          "AverageLifeDuration": "PT34.9S",
          "GrenadeKills": 1,
          "HeadshotKills": 31,
          "MeleeKills": 9,
          "PowerWeaponKills": 2,
          "ShotsFired": 765,
          "ShotsHit": 414,
          "Accuracy": 54.11,
          "DamageDealt": 17828,
          "DamageTaken": 17953,
          "CalloutAssists": 6,
          "VehicleDestroys": 0,
          "DriverAssists": 0,
          "Hijacks": 0,
          "EmpAssists": 0,
          "MaxKillingSpree": 4,
          "Medals": [
            {
              "NameId": 1169571763,
              "Count": 5,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 1512363953,
              "Count": 5,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2123530881,
              "Count": 2,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 548533137,
              "Count": 3,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2852571933,
              "Count": 4,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 622331684,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 269174970,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 4229934157,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            },
            {
              "NameId": 2477555653,
              "Count": 1,
              "TotalPersonalScoreAwarded": 0
            }
          ],
          "PersonalScores": [
            {
              "NameId": 249491819,
              "Count": 1,
              "TotalPersonalScoreAwarded": -100
            },
            {
              "NameId": 1024030246,
              "Count": 52,
              "TotalPersonalScoreAwarded": 5200
            },
            {
              "NameId": 638246808,
              "Count": 22,
              "TotalPersonalScoreAwarded": 1100
            },
            {
              "NameId": 152718958,
              "Count": 6,
              "TotalPersonalScoreAwarded": 60
            },
            {
              "NameId": 911992497,
              "Count": 1,
              "TotalPersonalScoreAwarded": -100
            }
          ],
          "DeprecatedDamageDealt": 17828.0,
          "DeprecatedDamageTaken": 17953.0,
          "Spawns": 52,
          "ObjectivesCompleted": 0
        },
        "PvpStats": {
          "Kills": 52,
          "Deaths": 49,
          "Assists": 22,
          "KDA": 10.33
        }
      }
    }
  ],
  "Players": [
    {
      "PlayerId": "xuid(2535446567488589)",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 1,
      "Outcome": 2,
      "Rank": 2,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-05T12:51:56.129Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT9M49.453S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 1,
          "Stats": {
            "CoreStats": {
              "Score": 13,
              "PersonalScore": 1550,
              "RoundsWon": 1,
              "RoundsLost": 0,
              "RoundsTied": 0,
              "Kills": 13,
              "Deaths": 15,
              "Assists": 5,
              "KDA": -0.33,
              "Suicides": 0,
              "Betrayals": 0,
              "AverageLifeDuration": "PT26.8S",
              "GrenadeKills": 1,
              "HeadshotKills": 8,
              "MeleeKills": 2,
              "PowerWeaponKills": 0,
              "ShotsFired": 152,
              "ShotsHit": 94,
              "Accuracy": 61.84,
              "DamageDealt": 4318,
              "DamageTaken": 5546,
              "CalloutAssists": 0,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 2,
              "Medals": [
                {
                  "NameId": 1512363953,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 1024030246,
                  "Count": 13,
                  "TotalPersonalScoreAwarded": 1300
                },
                {
                  "NameId": 638246808,
                  "Count": 5,
                  "TotalPersonalScoreAwarded": 250
                }
              ],
              "DeprecatedDamageDealt": 4318.0,
              "DeprecatedDamageTaken": 5546.0,
              "Spawns": 16,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 13,
              "Deaths": 15,
              "Assists": 5,
              "KDA": -0.33
            }
          }
        }
      ]
    },
    {
      "PlayerId": "xuid(2533274878524261)",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 0,
      "Outcome": 3,
      "Rank": 6,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-05T12:51:56.142Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT9M49.453S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 0,
          "Stats": {
            "CoreStats": {
              "Score": 12,
              "PersonalScore": 1500,
              "RoundsWon": 0,
              "RoundsLost": 1,
              "RoundsTied": 0,
              "Kills": 12,
              "Deaths": 14,
              "Assists": 6,
              "KDA": 0.0,
              "Suicides": 0,
              "Betrayals": 0,
              "AverageLifeDuration": "PT31.8S",
              "GrenadeKills": 1,
              "HeadshotKills": 8,
              "MeleeKills": 1,
              "PowerWeaponKills": 5,
              "ShotsFired": 181,
              "ShotsHit": 98,
              "Accuracy": 54.14,
              "DamageDealt": 5316,
              "DamageTaken": 4001,
              "CalloutAssists": 0,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 4,
              "Medals": [
                {
                  "NameId": 4229934157,
                  "Count": 3,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 622331684,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2414983178,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2602963073,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 4277328263,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 548533137,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 1024030246,
                  "Count": 12,
                  "TotalPersonalScoreAwarded": 1200
                },
                {
                  "NameId": 638246808,
                  "Count": 6,
                  "TotalPersonalScoreAwarded": 300
                }
              ],
              "DeprecatedDamageDealt": 5316.0,
              "DeprecatedDamageTaken": 4001.0,
              "Spawns": 14,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 12,
              "Deaths": 14,
              "Assists": 6,
              "KDA": 0.0
            }
          }
        }
      ]
    },
    {
      "PlayerId": "xuid(2533274843031719)",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 1,
      "Outcome": 2,
      "Rank": 3,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-05T12:51:56.142Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT9M49.453S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 1,
          "Stats": {
            "CoreStats": {
              "Score": 12,
              "PersonalScore": 1250,
              "RoundsWon": 1,
              "RoundsLost": 0,
              "RoundsTied": 0,
              "Kills": 12,
              "Deaths": 12,
              "Assists": 1,
              "KDA": 0.33,
              "Suicides": 0,
              "Betrayals": 0,
              "AverageLifeDuration": "PT34.9S",
              "GrenadeKills": 0,
              "HeadshotKills": 8,
              "MeleeKills": 2,
              "PowerWeaponKills": 0,
              "ShotsFired": 209,
              "ShotsHit": 106,
              "Accuracy": 50.71,
              "DamageDealt": 4561,
              "DamageTaken": 4391,
              "CalloutAssists": 0,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 4,
              "Medals": [
                {
                  "NameId": 2123530881,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 1169571763,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 1024030246,
                  "Count": 12,
                  "TotalPersonalScoreAwarded": 1200
                },
                {
                  "NameId": 638246808,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 50
                }
              ],
              "DeprecatedDamageDealt": 4561.0,
              "DeprecatedDamageTaken": 4391.0,
              "Spawns": 13,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 12,
              "Deaths": 12,
              "Assists": 1,
              "KDA": 0.33
            }
          }
        }
      ]
    },
    {
      "PlayerId": "xuid(2533274861785174)",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 0,
      "Outcome": 3,
      "Rank": 8,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-05T12:51:56.142Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT9M49.453S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 0,
          "Stats": {
            "CoreStats": {
              "Score": 8,
              "PersonalScore": 1220,
              "RoundsWon": 0,
              "RoundsLost": 1,
              "RoundsTied": 0,
              "Kills": 8,
              "Deaths": 11,
              "Assists": 8,
              "KDA": -0.33,
              "Suicides": 0,
              "Betrayals": 0,
              "AverageLifeDuration": "PT38.5S",
              "GrenadeKills": 0,
              "HeadshotKills": 7,
              "MeleeKills": 1,
              "PowerWeaponKills": 0,
              "ShotsFired": 183,
              "ShotsHit": 103,
              "Accuracy": 56.28,
              "DamageDealt": 4357,
              "DamageTaken": 4135,
              "CalloutAssists": 2,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 2,
              "Medals": [
                {
                  "NameId": 548533137,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 1169571763,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 1512363953,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 1024030246,
                  "Count": 8,
                  "TotalPersonalScoreAwarded": 800
                },
                {
                  "NameId": 638246808,
                  "Count": 8,
                  "TotalPersonalScoreAwarded": 400
                },
                {
                  "NameId": 152718958,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 20
                }
              ],
              "DeprecatedDamageDealt": 4357.0,
              "DeprecatedDamageTaken": 4135.0,
              "Spawns": 12,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 8,
              "Deaths": 11,
              "Assists": 8,
              "KDA": -0.33
            }
          }
        }
      ]
    },
    {
      "PlayerId": "xuid({YOUR_XUID})",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 1,
      "Outcome": 2,
      "Rank": 4,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-05T12:51:56.142Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT9M49.453S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 1,
          "Stats": {
            "CoreStats": {
              "Score": 10,
              "PersonalScore": 1400,
              "RoundsWon": 1,
              "RoundsLost": 0,
              "RoundsTied": 0,
              "Kills": 10,
              "Deaths": 12,
              "Assists": 8,
              "KDA": 0.66,
              "Suicides": 0,
              "Betrayals": 0,
              "AverageLifeDuration": "PT34.9S",
              "GrenadeKills": 0,
              "HeadshotKills": 6,
              "MeleeKills": 0,
              "PowerWeaponKills": 0,
              "ShotsFired": 174,
              "ShotsHit": 93,
              "Accuracy": 53.44,
              "DamageDealt": 3459,
              "DamageTaken": 4347,
              "CalloutAssists": 0,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 3,
              "Medals": [
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 622331684,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 1024030246,
                  "Count": 10,
                  "TotalPersonalScoreAwarded": 1000
                },
                {
                  "NameId": 638246808,
                  "Count": 8,
                  "TotalPersonalScoreAwarded": 400
                }
              ],
              "DeprecatedDamageDealt": 3459.0,
              "DeprecatedDamageTaken": 4347.0,
              "Spawns": 13,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 10,
              "Deaths": 12,
              "Assists": 8,
              "KDA": 0.66
            }
          }
        }
      ]
    },
    {
      "PlayerId": "xuid(2535422334806406)",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 1,
      "Outcome": 2,
      "Rank": 1,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-05T12:51:56.142Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT9M49.453S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 1,
          "Stats": {
            "CoreStats": {
              "Score": 15,
              "PersonalScore": 1960,
              "RoundsWon": 1,
              "RoundsLost": 0,
              "RoundsTied": 0,
              "Kills": 17,
              "Deaths": 10,
              "Assists": 8,
              "KDA": 9.66,
              "Suicides": 1,
              "Betrayals": 1,
              "AverageLifeDuration": "PT47.6S",
              "GrenadeKills": 0,
              "HeadshotKills": 9,
              "MeleeKills": 5,
              "PowerWeaponKills": 2,
              "ShotsFired": 230,
              "ShotsHit": 121,
              "Accuracy": 52.6,
              "DamageDealt": 5490,
              "DamageTaken": 3669,
              "CalloutAssists": 6,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 4,
              "Medals": [
                {
                  "NameId": 1169571763,
                  "Count": 4,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 1512363953,
                  "Count": 3,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 548533137,
                  "Count": 3,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 269174970,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 4229934157,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2477555653,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 249491819,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": -100
                },
                {
                  "NameId": 1024030246,
                  "Count": 17,
                  "TotalPersonalScoreAwarded": 1700
                },
                {
                  "NameId": 638246808,
                  "Count": 8,
                  "TotalPersonalScoreAwarded": 400
                },
                {
                  "NameId": 152718958,
                  "Count": 6,
                  "TotalPersonalScoreAwarded": 60
                },
                {
                  "NameId": 911992497,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": -100
                }
              ],
              "DeprecatedDamageDealt": 5490.0,
              "DeprecatedDamageTaken": 3669.0,
              "Spawns": 10,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 17,
              "Deaths": 10,
              "Assists": 8,
              "KDA": 9.66
            }
          }
        }
      ]
    },
    {
      "PlayerId": "xuid(2535455520021619)",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 0,
      "Outcome": 3,
      "Rank": 6,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-05T12:51:56.142Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT9M49.453S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 0,
          "Stats": {
            "CoreStats": {
              "Score": 12,
              "PersonalScore": 1420,
              "RoundsWon": 0,
              "RoundsLost": 1,
              "RoundsTied": 0,
              "Kills": 12,
              "Deaths": 15,
              "Assists": 4,
              "KDA": -1.66,
              "Suicides": 0,
              "Betrayals": 0,
              "AverageLifeDuration": "PT28.8S",
              "GrenadeKills": 2,
              "HeadshotKills": 5,
              "MeleeKills": 2,
              "PowerWeaponKills": 0,
              "ShotsFired": 191,
              "ShotsHit": 85,
              "Accuracy": 44.5,
              "DamageDealt": 3526,
              "DamageTaken": 5129,
              "CalloutAssists": 2,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 4,
              "Medals": [
                {
                  "NameId": 3334154676,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 638246808,
                  "Count": 4,
                  "TotalPersonalScoreAwarded": 200
                },
                {
                  "NameId": 1024030246,
                  "Count": 12,
                  "TotalPersonalScoreAwarded": 1200
                },
                {
                  "NameId": 152718958,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 20
                }
              ],
              "DeprecatedDamageDealt": 3526.0,
              "DeprecatedDamageTaken": 5129.0,
              "Spawns": 15,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 12,
              "Deaths": 15,
              "Assists": 4,
              "KDA": -1.66
            }
          }
        }
      ]
    },
    {
      "PlayerId": "xuid(2535416229856322)",
      "PlayerType": 1,
      "BotAttributes": null,
      "LastTeamId": 0,
      "Outcome": 3,
      "Rank": 5,
      "ParticipationInfo": {
        "FirstJoinedTime": "2026-05-05T12:51:56.142Z",
        "LastLeaveTime": null,
        "PresentAtBeginning": true,
        "JoinedInProgress": false,
        "LeftInProgress": false,
        "PresentAtCompletion": true,
        "TimePlayed": "PT9M49.453S",
        "ConfirmedParticipation": null
      },
      "PlayerTeamStats": [
        {
          "TeamId": 0,
          "Stats": {
            "CoreStats": {
              "Score": 15,
              "PersonalScore": 1670,
              "RoundsWon": 0,
              "RoundsLost": 1,
              "RoundsTied": 0,
              "Kills": 15,
              "Deaths": 12,
              "Assists": 3,
              "KDA": 4.0,
              "Suicides": 0,
              "Betrayals": 0,
              "AverageLifeDuration": "PT34.9S",
              "GrenadeKills": 1,
              "HeadshotKills": 9,
              "MeleeKills": 3,
              "PowerWeaponKills": 0,
              "ShotsFired": 149,
              "ShotsHit": 78,
              "Accuracy": 52.34,
              "DamageDealt": 3551,
              "DamageTaken": 4581,
              "CalloutAssists": 2,
              "VehicleDestroys": 0,
              "DriverAssists": 0,
              "Hijacks": 0,
              "EmpAssists": 0,
              "MaxKillingSpree": 4,
              "Medals": [
                {
                  "NameId": 1512363953,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 1169571763,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 2852571933,
                  "Count": 1,
                  "TotalPersonalScoreAwarded": 0
                },
                {
                  "NameId": 622331684,
                  "Count": 3,
                  "TotalPersonalScoreAwarded": 0
                }
              ],
              "PersonalScores": [
                {
                  "NameId": 638246808,
                  "Count": 3,
                  "TotalPersonalScoreAwarded": 150
                },
                {
                  "NameId": 1024030246,
                  "Count": 15,
                  "TotalPersonalScoreAwarded": 1500
                },
                {
                  "NameId": 152718958,
                  "Count": 2,
                  "TotalPersonalScoreAwarded": 20
                }
              ],
              "DeprecatedDamageDealt": 3551.0,
              "DeprecatedDamageTaken": 4581.0,
              "Spawns": 13,
              "ObjectivesCompleted": 0
            },
            "PvpStats": {
              "Kills": 15,
              "Deaths": 12,
              "Assists": 3,
              "KDA": 4.0
            }
          }
        }
      ]
    }
  ]
}
  ```


## Table: `OperationRewardTracks`

### Schema
```sql
CREATE TABLE OperationRewardTracks (

	ResponseBody TEXT,

	Path TEXT,

	LastUpdated DATETIME,

	TrackId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.TrackId')) VIRTUAL,

	XpPerRank Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.XpPerRank')) VIRTUAL,

	HideIfNotOwned Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.HideIfNotOwned')) VIRTUAL,

	Ranks Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Ranks')) VIRTUAL,

	Name Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Name')) VIRTUAL,

	Description Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,

	OperationNumber Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.OperationNumber')) VIRTUAL,

	DateRange Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.DateRange')) VIRTUAL,

	IsRitual Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.IsRitual')) VIRTUAL,

	SummaryImagePath Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.SummaryImagePath')) VIRTUAL,

	WeekNumber Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.WeekNumber')) VIRTUAL,

	BackgroundImagePath Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.BackgroundImagePath')) VIRTUAL

)
```

**Records: 31**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "TrackId": "S13Op01",
  "XpPerRank": 1000,
  "Ranks": [
    {
      "Rank": 1,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/wristattachments/4241927-ArmorWristAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorWristAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 2,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/emblems/104-001-popculture-de-8643a9b3.json",
            "Amount": 1,
            "Type": "SpartanEmblem"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      }
    },
    {
      "Rank": 3,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/kneepads/4256990-ArmorKneePad-Mark-V-B.json",
            "Amount": 1,
            "Type": "ArmorKneePad"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/backdropimages/3849616-SpartanBackdropImage.json",
            "Amount": 1,
            "Type": "SpartanBackdropImage"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 4,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/ai/colors/301-100-epic-tangerin-e00ccb9a.json",
            "Amount": 1,
            "Type": "AiColor"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 5,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/chestattachments/4256956-ArmorChestAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorChestAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 6,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/wristattachments/4241935-ArmorWristAttachment-Mark-V-B.json",
            "Amount": 1,
            "Type": "ArmorWristAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 7,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/emblems/3849634-SpartanEmblem.json",
            "Amount": 1,
            "Type": "SpartanEmblem"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 8,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/hipattachments/4256957-ArmorHipAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHipAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 9,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/203-208-olympus-83efab8f.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 10,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Coatings/4256960-ArmorCoating-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 11,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/hipattachments/4256989-ArmorHipAttachment-Mark-V-B.json",
            "Amount": 1,
            "Type": "ArmorHipAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 12,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/kneepads/4256958-ArmorKneePad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorKneePad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 13,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/actionposes/101-000-menu-stance-r-fab2a4da.json",
            "Amount": 1,
            "Type": "SpartanActionPose"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 14,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/shouldersleft/4256955-ArmorLeftShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorLeftShoulderPad"
          },
          {
            "InventoryItemPath": "Inventory/armor/shouldersright/4256955-ArmorRightShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorRightShoulderPad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 15,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/helmets/4256959-ArmorHelmet-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmet"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 16,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/chestattachments/4256988-ArmorChestAttachment-Mark-V-B.json",
            "Amount": 1,
            "Type": "ArmorChestAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 17,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/HelmetAttachments/4256954-ArmorHelmetAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmetAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 18,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Vehicle/coatings/404-300-olympus-0fd929ef.json",
            "Amount": 1,
            "Type": "VehicleCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 19,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/3839978-WeaponCoating-BR75-Battle-Rifle.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 20,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Coatings/4256992-ArmorCoating-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorCoating"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/alternategeos/3839977-WeaponAlternateGeometryRegion-BR75-Battle-Rifle.json",
            "Amount": 1,
            "Type": "WeaponAlternateGeometryRegion"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 21,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/shouldersleft/4256987-ArmorLeftShoulderPad-Mark-V-B.json",
            "Amount": 1,
            "Type": "ArmorLeftShoulderPad"
          },
          {
            "InventoryItemPath": "Inventory/armor/shouldersright/4256987-ArmorRightShoulderPad-Mark-V-B.json",
            "Amount": 1,
            "Type": "ArmorRightShoulderPad"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 22,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/backdropimages/3849609-SpartanBackdropImage.json",
            "Amount": 1,
            "Type": "SpartanBackdropImage"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 23,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/emblems/3849635-SpartanEmblem.json",
            "Amount": 1,
            "Type": "SpartanEmblem"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 24,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/kneepads/4256965-ArmorKneePad-Chimera.json",
            "Amount": 1,
            "Type": "ArmorKneePad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 25,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/helmets/4256991-ArmorHelmet-Mark-V-B.json",
            "Amount": 1,
            "Type": "ArmorHelmet"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/chestattachments/4256963-ArmorChestAttachment-Chimera.json",
            "Amount": 1,
            "Type": "ArmorChestAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 26,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/HelmetAttachments/4256986-ArmorHelmetAttachment-Mark-V-B.json",
            "Amount": 1,
            "Type": "ArmorHelmetAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 27,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/charms/3759995-WeaponCharm.json",
            "Amount": 1,
            "Type": "WeaponCharm"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 28,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/visors/012-001-1fd9a6d3.json",
            "Amount": 1,
            "Type": "ArmorVisor"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 29,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/wristattachments/4241928-ArmorWristAttachment-Chimera.json",
            "Amount": 1,
            "Type": "ArmorWristAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 30,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Coatings/4256967-ArmorCoating-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 31,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/emblems/3849632-SpartanEmblem.json",
            "Amount": 1,
            "Type": "SpartanEmblem"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 32,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/hipattachments/4256964-ArmorHipAttachment-Chimera.json",
            "Amount": 1,
            "Type": "ArmorHipAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 33,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/203-207-olympus-1f0a3a10.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 34,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/shouldersleft/4256962-ArmorLeftShoulderPad-Chimera.json",
            "Amount": 1,
            "Type": "ArmorLeftShoulderPad"
          },
          {
            "InventoryItemPath": "Inventory/armor/shouldersright/4256962-ArmorRightShoulderPad-Chimera.json",
            "Amount": 1,
            "Type": "ArmorRightShoulderPad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 35,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/helmets/4256966-ArmorHelmet-Chimera.json",
            "Amount": 1,
            "Type": "ArmorHelmet"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 36,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/kneepads/4256944-ArmorKneePad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorKneePad"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 37,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Vehicle/coatings/404-303-olympus-457f8aa3.json",
            "Amount": 1,
            "Type": "VehicleCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 38,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/HelmetAttachments/4256961-ArmorHelmetAttachment-Chimera.json",
            "Amount": 1,
            "Type": "ArmorHelmetAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 39,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/4257011-WeaponCoating-BR75-Battle-Rifle.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 40,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/alternategeos/4256969-WeaponAlternateGeometryRegion-Needler.json",
            "Amount": 1,
            "Type": "WeaponAlternateGeometryRegion"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 41,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/hipattachments/4256943-ArmorHipAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHipAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 42,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/backdropimages/103-000-ui-background-78fa3a6a.json",
            "Amount": 1,
            "Type": "SpartanBackdropImage"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 43,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/emblems/3849633-SpartanEmblem.json",
            "Amount": 1,
            "Type": "SpartanEmblem"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 44,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/kneepads/4256983-ArmorKneePad-Rakshasa.json",
            "Amount": 1,
            "Type": "ArmorKneePad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 45,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/chestattachments/4256981-ArmorChestAttachment-Rakshasa.json",
            "Amount": 1,
            "Type": "ArmorChestAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 46,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/visors/012-001-9448e41a.json",
            "Amount": 1,
            "Type": "ArmorVisor"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 47,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/chestattachments/4256942-ArmorChestAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorChestAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 48,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/charms/201-201-6b2244aa.json",
            "Amount": 1,
            "Type": "WeaponCharm"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 49,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/wristattachments/4241936-ArmorWristAttachment-Rakshasa.json",
            "Amount": 1,
            "Type": "ArmorWristAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 50,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/wristattachments/4241926-ArmorWristAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorWristAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Coatings/4256985-ArmorCoating-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 51,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/203-202-olympus-a90e08e9.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 52,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/hipattachments/4256982-ArmorHipAttachment-Rakshasa.json",
            "Amount": 1,
            "Type": "ArmorHipAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 53,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Vehicle/coatings/404-300-olympus-42059505.json",
            "Amount": 1,
            "Type": "VehicleCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 54,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/shouldersleft/4256980-ArmorLeftShoulderPad-Rakshasa.json",
            "Amount": 1,
            "Type": "ArmorLeftShoulderPad"
          },
          {
            "InventoryItemPath": "Inventory/armor/shouldersright/4256980-ArmorRightShoulderPad-Rakshasa.json",
            "Amount": 1,
            "Type": "ArmorRightShoulderPad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 55,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Coatings/4256945-ArmorCoating-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorCoating"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/helmets/4256984-ArmorHelmet-Rakshasa.json",
            "Amount": 1,
            "Type": "ArmorHelmet"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 56,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/shouldersleft/4256941-ArmorLeftShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorLeftShoulderPad"
          },
          {
            "InventoryItemPath": "Inventory/armor/shouldersright/4256941-ArmorRightShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorRightShoulderPad"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 57,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/HelmetAttachments/4256979-ArmorHelmetAttachment-Rakshasa.json",
            "Amount": 1,
            "Type": "ArmorHelmetAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 58,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/visors/012-001-87d4f660.json",
            "Amount": 1,
            "Type": "ArmorVisor"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 59,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/4257012-WeaponCoating-BR75-Battle-Rifle.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 60,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/alternategeos/4256970-WeaponAlternateGeometryRegion-Heatwave.json",
            "Amount": 1,
            "Type": "WeaponAlternateGeometryRegion"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 61,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/helmets/4256939-ArmorHelmet-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmet"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 62,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/HelmetAttachments/4256940-ArmorHelmetAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmetAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 63,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/backdropimages/103-000-ui-background-1c96ff6e.json",
            "Amount": 1,
            "Type": "SpartanBackdropImage"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 64,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/kneepads/4256977-ArmorKneePad-Mark-IV.json",
            "Amount": 1,
            "Type": "ArmorKneePad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 65,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/chestattachments/4256976-ArmorChestAttachment-Mark-IV.json",
            "Amount": 1,
            "Type": "ArmorChestAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 66,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/emblems/104-001-olympus-sunra-b1c97db1.json",
            "Amount": 1,
            "Type": "SpartanEmblem"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      }
    },
    {
      "Rank": 67,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/charms/3760005-WeaponCharm.json",
            "Amount": 1,
            "Type": "WeaponCharm"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 68,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/wristattachments/4241933-ArmorWristAttachment-Mark-IV.json",
            "Amount": 1,
            "Type": "ArmorWristAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 69,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/203-202-olympus-3aa90e26.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 70,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/backdropimages/103-000-ui-background-4acc58e8.json",
            "Amount": 1,
            "Type": "SpartanBackdropImage"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Coatings/4256978-ArmorCoating-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 71,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/kneepads/4256912-ArmorKneePad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorKneePad"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 72,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/emblems/104-001-spi-ilustrati-7b35b809.json",
            "Amount": 1,
            "Type": "SpartanEmblem"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 73,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/hipattachments/4367742-ArmorHipAttachment-Mark-IV.json",
            "Amount": 1,
            "Type": "ArmorHipAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 74,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/shouldersleft/4256975-ArmorLeftShoulderPad-Mark-IV.json",
            "Amount": 1,
            "Type": "ArmorLeftShoulderPad"
          },
          {
            "InventoryItemPath": "Inventory/armor/shouldersright/4256975-ArmorRightShoulderPad-Mark-IV.json",
            "Amount": 1,
            "Type": "ArmorRightShoulderPad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 75,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/helmets/4256973-ArmorHelmet-Mark-IV.json",
            "Amount": 1,
            "Type": "ArmorHelmet"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 76,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/wristattachments/4241929-ArmorWristAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorWristAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 77,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/charms/3760003-WeaponCharm.json",
            "Amount": 1,
            "Type": "WeaponCharm"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 78,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/HelmetAttachments/4256974-ArmorHelmetAttachment-Mark-IV.json",
            "Amount": 1,
            "Type": "ArmorHelmetAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 79,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/4257006-WeaponCoating-BR75-Battle-Rifle.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 80,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/emblems/104-001-popculture-th-d1acc6f9.json",
            "Amount": 1,
            "Type": "SpartanEmblem"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/alternategeos/4257003-WeaponAlternateGeometryRegion-S7-Sniper.json",
            "Amount": 1,
            "Type": "WeaponAlternateGeometryRegion"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 81,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/hipattachments/4256911-ArmorHipAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHipAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 82,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/backdropimages/103-000-ui-background-058dce2f.json",
            "Amount": 1,
            "Type": "SpartanBackdropImage"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 83,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/ai/colors/301-100-base-purple-d85a184d.json",
            "Amount": 1,
            "Type": "AiColor"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 84,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/kneepads/4256918-ArmorKneePad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorKneePad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 85,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/chestattachments/4256916-ArmorChestAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorChestAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 86,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/chestattachments/4256910-ArmorChestAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorChestAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 87,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/charms/3760000-WeaponCharm.json",
            "Amount": 1,
            "Type": "WeaponCharm"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 88,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/actionposes/101-000-menu-stance-o-406c9641.json",
            "Amount": 1,
            "Type": "SpartanActionPose"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 89,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/4257009-WeaponCoating-BR75-Battle-Rifle.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 90,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Coatings/4256913-ArmorCoating-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorCoating"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/alternategeos/4256936-WeaponAlternateGeometryRegion-Shock-Rifle.json",
            "Amount": 1,
            "Type": "WeaponAlternateGeometryRegion"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 91,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/shouldersleft/4256909-ArmorLeftShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorLeftShoulderPad"
          },
          {
            "InventoryItemPath": "Inventory/armor/shouldersright/4256909-ArmorRightShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorRightShoulderPad"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 92,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/emblems/3849636-SpartanEmblem.json",
            "Amount": 1,
            "Type": "SpartanEmblem"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 93,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/shouldersleft/4256915-ArmorLeftShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorLeftShoulderPad"
          },
          {
            "InventoryItemPath": "Inventory/armor/shouldersright/4256915-ArmorRightShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorRightShoulderPad"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 94,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/Coatings/203-202-olympus-3e1bfb6c.json",
            "Amount": 1,
            "Type": "WeaponCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 95,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/alternategeos/4024783-WeaponAlternateGeometryRegion-MK50-Sidekick.json",
            "Amount": 1,
            "Type": "WeaponAlternateGeometryRegion"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 96,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/helmets/4256907-ArmorHelmet-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmet"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      }
    },
    {
      "Rank": 97,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/HelmetAttachments/4256908-ArmorHelmetAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmetAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/wristattachments/4241930-ArmorWristAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorWristAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 98,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/hipattachments/4256917-ArmorHipAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHipAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 99,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Coatings/002-001-olympus-0f1e2897.json",
            "Amount": 1,
            "Type": "ArmorCoating"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Coatings/4256920-ArmorCoating-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorCoating"
          }
        ],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 100,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/spartan/actionposes/101-000-menu-stance-s-7ed51a2c.json",
            "Amount": 1,
            "Type": "SpartanActionPose"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/helmets/4256919-ArmorHelmet-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmet"
          },
          {
            "InventoryItemPath": "Inventory/armor/HelmetAttachments/4256914-ArmorHelmetAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmetAttachment"
          }
        ],
        "CurrencyRewards": []
      }
    }
  ],
  "Name": {
    "status": "Ready",
    "value": "Infinite",
    "translations": {
      "qps-ploc": "Ϊηƒïήίτĕ !!",
      "qps-ploca": "Ϊⁿƒïήīŧе !!",
      "qps-plocm": "İŋƒίńîŧė !!"
    }
  },
  "Description": {
    "status": "Test",
    "value": "",
    "translations": {}
  },
  "OperationNumber": 13001,
  "DateRange": {
    "status": "Test",
    "value": "",
    "translations": {}
  },
  "IsRitual": false,
  "SummaryImagePath": "",
  "WeekNumber": null,
  "BackgroundImagePath": "progression/RewardTracks/S13_Infinite_UI_BP_EVENT_WIDGET_986x248.png",
  "BattlePassImage": "progression/RewardTracks/S13_Infinite_SpartanMinor.png",
  "BattlePassBundleImage": "progression/RewardTracks/S13_Infinite_SpartanMajor.png",
  "HideIfNotOwned": false
}
  ```
- **Path**: `RewardTracks/Operations/S13Op01.json`
- **LastUpdated**: `2026-05-11T22:10:47.807+09:00`

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "TrackId": "S12Op03",
  "XpPerRank": 1000,
  "Ranks": [
    {
      "Rank": 1,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/Weapon/charms/201-201-3fe29f2d.json",
            "Amount": 1,
            "Type": "WeaponCharm"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 2,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 3,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 4,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 5,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/kneepads/4077072-ArmorKneePad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorKneePad"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 6,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 7,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 8,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 9,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 10,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/wristattachments/4241921-ArmorWristAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorWristAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 11,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 12,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 13,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 14,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 15,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/chestattachments/4077070-ArmorChestAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorChestAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 16,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 17,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 1000
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 18,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/shouldersleft/4077069-ArmorLeftShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorLeftShoulderPad"
          },
          {
            "InventoryItemPath": "Inventory/armor/shouldersright/4077069-ArmorRightShoulderPad-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorRightShoulderPad"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 19,
      "FreeRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": [
          {
            "CurrencyPath": "Currency/Currencies/softcurrency.json",
            "Amount": 2500
          }
        ]
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    },
    {
      "Rank": 20,
      "FreeRewards": {
        "InventoryRewards": [
          {
            "InventoryItemPath": "Inventory/armor/Helmets/4077067-ArmorHelmet-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmet"
          },
          {
            "InventoryItemPath": "Inventory/armor/HelmetAttachments/4077068-ArmorHelmetAttachment-Mark-VII.json",
            "Amount": 1,
            "Type": "ArmorHelmetAttachment"
          }
        ],
        "CurrencyRewards": []
      },
      "PaidRewards": {
        "InventoryRewards": [],
        "CurrencyRewards": []
      }
    }
  ],
  "Name": {
    "status": "Ready",
    "value": "Haloween II",
    "translations": {
      "cs-CZ": "Haloween II",
      "da-DK": "Haloween II",
      "de-DE": "Haloween II",
      "el-GR": "Haloween ΙΙ",
      "es-ES": "Haloween II",
      "es-MX": "Haloween II",
      "fi-FI": "Haloween II",
      "fr-FR": "Haloween II",
      "hu-HU": "Halloween II",
      "it-IT": "Haloween II",
      "ja-JP": "ハロウィン II",
      "ko-KR": "할로윈 II",
      "nb-NO": "Haloween II",
      "nl-NL": "Haloween II",
      "pl-PL": "Haloween II",
      "pt-BR": "Haloween II",
      "pt-PT": "Haloween II",
      "ru-RU": "Хэллоуин II",
      "sv-SE": "Haloween II",
      "tr-TR": "Halolar Bayramı II",
      "zh-CN": "光环万圣节 II",
      "zh-TW": "萬聖節 II",
      "qps-ploc": "Ĝŗзάť Ĵθûяиęŷ !!! ",
      "qps-ploca": "Ġѓêăŧ Јőµřήéў !!! ",
      "qps-plocm": "Ġяěάţ Јθύřⁿėŷ !!! "
    }
  },
  "Description": {
    "status": "Test",
    "value": "",
    "translations": {}
  },
  "OperationNumber": 12003,
  "DateRange": {
    "status": "Test",
    "value": "",
    "translations": {}
  },
  "IsRitual": false,
  "SummaryImagePath": "",
  "WeekNumber": null,
  "BackgroundImagePath": "progression/RewardTracks/S12_H2_UI_BP_EVENT_WIDGET_986x248.png",
  "BattlePassImage": "progression/RewardTracks/S12_H2_SpartanMinor.png",
  "BattlePassBundleImage": "progression/RewardTracks/S12_H2_SpartanMajor.png",
  "HideIfNotOwned": true
}
  ```
- **Path**: `RewardTracks/Operations/S12Op03.json`
- **LastUpdated**: `2026-05-11T22:10:48.467+09:00`


## Table: `OwnedInventoryItems`

### Schema
```sql
CREATE TABLE OwnedInventoryItems (

	Amount INTEGER,

	ItemId TEXT,

	ItemPath TEXT,

	ItemType TEXT,

	FirstAcquiredDate DATETIME

)
```

**Records: 7329**

### Sample Row 1

- **Amount**: `6`
- **ItemId**: `301-100-base-cyan-899ff22a`
- **ItemPath**: `Inventory/Ai/Colors/301-100-base-cyan-899ff22a.json`
- **ItemType**: `AiColor`
- **FirstAcquiredDate**: `2021-11-16 12:30:10.286`

### Sample Row 2

- **Amount**: `6`
- **ItemId**: `301-100-base-orange-58e3a39b`
- **ItemPath**: `Inventory/Ai/Colors/301-100-base-orange-58e3a39b.json`
- **ItemType**: `AiColor`
- **FirstAcquiredDate**: `2021-11-16 12:30:10.286`


## Table: `PlayerMatchStats`

### Schema
```sql
CREATE TABLE PlayerMatchStats (

	ResponseBody TEXT,

	MatchId TEXT,

	PlayerStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Value')) VIRTUAL

)
```

**Records: 3366**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "Value": [
    {
      "Id": "xuid({YOUR_XUID})",
      "ResultCode": 1,
      "Result": {
        "TeamMmr": 0.0,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 0,
            "MeasurementMatchesRemaining": 0,
            "Tier": "",
            "TierStart": 0,
            "SubTier": 0,
            "NextTier": "",
            "NextTierStart": 0,
            "NextSubTier": 0,
            "InitialMeasurementMatches": 0,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 0
          },
          "PostMatchCsr": {
            "Value": 0,
            "MeasurementMatchesRemaining": 0,
            "Tier": "",
            "TierStart": 0,
            "SubTier": 0,
            "NextTier": "",
            "NextTierStart": 0,
            "NextSubTier": 0,
            "InitialMeasurementMatches": 0,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 0
          }
        },
        "StatPerformances": {},
        "TeamId": 0,
        "TeamMmrs": {},
        "RankedRewards": null,
        "Counterfactuals": null
      }
    },
    {
      "Id": "xuid(2533274962782816)",
      "ResultCode": 1,
      "Result": {
        "TeamMmr": 0.0,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 0,
            "MeasurementMatchesRemaining": 0,
            "Tier": "",
            "TierStart": 0,
            "SubTier": 0,
            "NextTier": "",
            "NextTierStart": 0,
            "NextSubTier": 0,
            "InitialMeasurementMatches": 0,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 0
          },
          "PostMatchCsr": {
            "Value": 0,
            "MeasurementMatchesRemaining": 0,
            "Tier": "",
            "TierStart": 0,
            "SubTier": 0,
            "NextTier": "",
            "NextTierStart": 0,
            "NextSubTier": 0,
            "InitialMeasurementMatches": 0,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 0
          }
        },
        "StatPerformances": {},
        "TeamId": 0,
        "TeamMmrs": {},
        "RankedRewards": null,
        "Counterfactuals": null
      }
    }
  ]
}
  ```
- **MatchId**: `86c0de94-b42f-4926-ac40-19c39d3b0284`

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "Value": [
    {
      "Id": "xuid(2535446567488589)",
      "ResultCode": 0,
      "Result": {
        "TeamMmr": 1349.0048565602551,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 1299,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1250,
            "SubTier": 1,
            "NextTier": "Diamond",
            "NextTierStart": 1300,
            "NextSubTier": 2,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          },
          "PostMatchCsr": {
            "Value": 1306,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1300,
            "SubTier": 2,
            "NextTier": "Diamond",
            "NextTierStart": 1350,
            "NextSubTier": 3,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          }
        },
        "StatPerformances": {
          "Kills": {
            "Count": 13,
            "Expected": 13.363314206398446,
            "StdDev": 4.737273261227561
          },
          "Deaths": {
            "Count": 15,
            "Expected": 12.75761906317431,
            "StdDev": 4.52078439683331
          }
        },
        "TeamId": 0,
        "TeamMmrs": {
          "0": 1349.0048565602551,
          "1": 1265.0965428574646
        },
        "RankedRewards": null,
        "Counterfactuals": {
          "SelfCounterfactuals": {
            "Kills": 13.363314206398446,
            "Deaths": 12.75761906317431
          },
          "TierCounterfactuals": {
            "Bronze": {
              "Kills": -0.5125080516421896,
              "Deaths": 17.56341220598733
            },
            "Silver": {
              "Kills": 1.0950483400690962,
              "Deaths": 16.494572340578127
            },
            "Gold": {
              "Kills": 4.252225837225755,
              "Deaths": 15.442193178797003
            },
            "Platinum": {
              "Kills": 8.257973497104778,
              "Deaths": 14.308046431965147
            },
            "Diamond": {
              "Kills": 12.270524607511064,
              "Deaths": 13.103282671318068
            },
            "Onyx": {
              "Kills": 16.011204209770074,
              "Deaths": 11.899387418773188
            }
          }
        }
      }
    },
    {
      "Id": "xuid(2533274878524261)",
      "ResultCode": 0,
      "Result": {
        "TeamMmr": 1265.0965428574646,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 1447,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1400,
            "SubTier": 4,
            "NextTier": "Diamond",
            "NextTierStart": 1450,
            "NextSubTier": 5,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          },
          "PostMatchCsr": {
            "Value": 1437,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1400,
            "SubTier": 4,
            "NextTier": "Diamond",
            "NextTierStart": 1450,
            "NextSubTier": 5,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          }
        },
        "StatPerformances": {
          "Kills": {
            "Count": 12,
            "Expected": 13.95357378124309,
            "StdDev": 4.726321069033618
          },
          "Deaths": {
            "Count": 14,
            "Expected": 12.990753806040612,
            "StdDev": 4.516478686083677
          }
        },
        "TeamId": 1,
        "TeamMmrs": {
          "0": 1349.0048565602551,
          "1": 1265.0965428574646
        },
        "RankedRewards": null,
        "Counterfactuals": {
          "SelfCounterfactuals": {
            "Kills": 13.95357378124309,
            "Deaths": 12.990753806040612
          },
          "TierCounterfactuals": {
            "Bronze": {
              "Kills": -0.5956682423055286,
              "Deaths": 18.12466919789759
            },
            "Silver": {
              "Kills": 0.7612092986619428,
              "Deaths": 17.056415452794504
            },
            "Gold": {
              "Kills": 3.745607513845483,
              "Deaths": 16.00520228949647
            },
            "Platinum": {
              "Kills": 7.734806181256981,
              "Deaths": 14.8734644424393
            },
            "Diamond": {
              "Kills": 11.787296609665722,
              "Deaths": 13.673374111722996
            },
            "Onyx": {
              "Kills": 15.544505400137805,
              "Deaths": 12.477258405464855
            }
          }
        }
      }
    },
    {
      "Id": "xuid(2533274843031719)",
      "ResultCode": 0,
      "Result": {
        "TeamMmr": 1349.0048565602551,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 1261,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1250,
            "SubTier": 1,
            "NextTier": "Diamond",
            "NextTierStart": 1300,
            "NextSubTier": 2,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          },
          "PostMatchCsr": {
            "Value": 1276,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1250,
            "SubTier": 1,
            "NextTier": "Diamond",
            "NextTierStart": 1300,
            "NextSubTier": 2,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          }
        },
        "StatPerformances": {
          "Kills": {
            "Count": 12,
            "Expected": 13.809083731390862,
            "StdDev": 4.7355169057766355
          },
          "Deaths": {
            "Count": 12,
            "Expected": 12.614762620024504,
            "StdDev": 4.5250201606120815
          }
        },
        "TeamId": 0,
        "TeamMmrs": {
          "0": 1349.0048565602551,
          "1": 1265.0965428574646
        },
        "RankedRewards": null,
        "Counterfactuals": {
          "SelfCounterfactuals": {
            "Kills": 13.809083731390862,
            "Deaths": 12.614762620024504
          },
          "TierCounterfactuals": {
            "Bronze": {
              "Kills": -0.4299270608548417,
              "Deaths": 17.451806746722756
            },
            "Silver": {
              "Kills": 1.36827407703477,
              "Deaths": 16.382816190048317
            },
            "Gold": {
              "Kills": 4.638940055285826,
              "Deaths": 15.330143992323864
            },
            "Platinum": {
              "Kills": 8.64679296163129,
              "Deaths": 14.195406608331483
            },
            "Diamond": {
              "Kills": 12.631480601842334,
              "Deaths": 12.98952847957761
            },
            "Onyx": {
              "Kills": 16.362248258862053,
              "Deaths": 11.783834742120296
            }
          }
        }
      }
    },
    {
      "Id": "xuid(2533274861785174)",
      "ResultCode": 0,
      "Result": {
        "TeamMmr": 1265.0965428574646,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 1198,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Platinum",
            "TierStart": 1150,
            "SubTier": 5,
            "NextTier": "Diamond",
            "NextTierStart": 1200,
            "NextSubTier": 0,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          },
          "PostMatchCsr": {
            "Value": 1189,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Platinum",
            "TierStart": 1150,
            "SubTier": 5,
            "NextTier": "Diamond",
            "NextTierStart": 1200,
            "NextSubTier": 0,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          }
        },
        "StatPerformances": {
          "Kills": {
            "Count": 8,
            "Expected": 11.298478860527853,
            "StdDev": 4.79986907812572
          },
          "Deaths": {
            "Count": 11,
            "Expected": 13.82394988803726,
            "StdDev": 4.501103544997685
          }
        },
        "TeamId": 1,
        "TeamMmrs": {
          "0": 1349.0048565602551,
          "1": 1265.0965428574646
        },
        "RankedRewards": null,
        "Counterfactuals": {
          "SelfCounterfactuals": {
            "Kills": 11.298478860527853,
            "Deaths": 13.82394988803726
          },
          "TierCounterfactuals": {
            "Bronze": {
              "Kills": -0.5955406473969275,
              "Deaths": 18.124669663038453
            },
            "Silver": {
              "Kills": 0.7612412247977427,
              "Deaths": 17.056416475432734
            },
            "Gold": {
              "Kills": 3.745984880489094,
              "Deaths": 16.005204371909986
            },
            "Platinum": {
              "Kills": 7.735286119460195,
              "Deaths": 14.87346860496563
            },
            "Diamond": {
              "Kills": 11.787503890595904,
              "Deaths": 13.673382077238479
            },
            "Onyx": {
              "Kills": 15.544544768721694,
              "Deaths": 12.477272297222909
            }
          }
        }
      }
    },
    {
      "Id": "xuid({YOUR_XUID})",
      "ResultCode": 0,
      "Result": {
        "TeamMmr": 1349.0048565602551,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 1303,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1300,
            "SubTier": 2,
            "NextTier": "Diamond",
            "NextTierStart": 1350,
            "NextSubTier": 3,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          },
          "PostMatchCsr": {
            "Value": 1309,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1300,
            "SubTier": 2,
            "NextTier": "Diamond",
            "NextTierStart": 1350,
            "NextSubTier": 3,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          }
        },
        "StatPerformances": {
          "Kills": {
            "Count": 10,
            "Expected": 13.351918443026378,
            "StdDev": 4.738350834040862
          },
          "Deaths": {
            "Count": 12,
            "Expected": 12.761231305169604,
            "StdDev": 4.520787506367373
          }
        },
        "TeamId": 0,
        "TeamMmrs": {
          "0": 1349.0048565602551,
          "1": 1265.0965428574646
        },
        "RankedRewards": null,
        "Counterfactuals": {
          "SelfCounterfactuals": {
            "Kills": 13.351918443026378,
            "Deaths": 12.761231305169604
          },
          "TierCounterfactuals": {
            "Bronze": {
              "Kills": -0.5125477813712415,
              "Deaths": 17.563411871162085
            },
            "Silver": {
              "Kills": 1.095017371360811,
              "Deaths": 16.494571628579926
            },
            "Gold": {
              "Kills": 4.2520264961485115,
              "Deaths": 15.442191776955621
            },
            "Platinum": {
              "Kills": 8.257758023976704,
              "Deaths": 14.308043731522265
            },
            "Diamond": {
              "Kills": 12.27044161838818,
              "Deaths": 13.103277706737485
            },
            "Onyx": {
              "Kills": 16.011189893212826,
              "Deaths": 11.899379108222591
            }
          }
        }
      }
    },
    {
      "Id": "xuid(2535422334806406)",
      "ResultCode": 0,
      "Result": {
        "TeamMmr": 1349.0048565602551,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 1421,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1400,
            "SubTier": 4,
            "NextTier": "Diamond",
            "NextTierStart": 1450,
            "NextSubTier": 5,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          },
          "PostMatchCsr": {
            "Value": 1435,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1400,
            "SubTier": 4,
            "NextTier": "Diamond",
            "NextTierStart": 1450,
            "NextSubTier": 5,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          }
        },
        "StatPerformances": {
          "Kills": {
            "Count": 17,
            "Expected": 15.96995928868786,
            "StdDev": 4.72791980667859
          },
          "Deaths": {
            "Count": 10,
            "Expected": 11.912453050724732,
            "StdDev": 4.546478158876009
          }
        },
        "TeamId": 0,
        "TeamMmrs": {
          "0": 1349.0048565602551,
          "1": 1265.0965428574646
        },
        "RankedRewards": null,
        "Counterfactuals": {
          "SelfCounterfactuals": {
            "Kills": 15.96995928868786,
            "Deaths": 11.912453050724732
          },
          "TierCounterfactuals": {
            "Bronze": {
              "Kills": -0.4306142969141993,
              "Deaths": 17.45179709895658
            },
            "Silver": {
              "Kills": 1.3670747333674136,
              "Deaths": 16.382795832575134
            },
            "Gold": {
              "Kills": 4.633361905166104,
              "Deaths": 15.330104208066343
            },
            "Platinum": {
              "Kills": 8.641372113049522,
              "Deaths": 14.195330588408144
            },
            "Diamond": {
              "Kills": 12.629536979600688,
              "Deaths": 12.989389935643446
            },
            "Onyx": {
              "Kills": 16.36193083087525,
              "Deaths": 11.783604867268519
            }
          }
        }
      }
    },
    {
      "Id": "xuid(2535455520021619)",
      "ResultCode": 0,
      "Result": {
        "TeamMmr": 1265.0965428574646,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 1069,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Platinum",
            "TierStart": 1050,
            "SubTier": 3,
            "NextTier": "Platinum",
            "NextTierStart": 1100,
            "NextSubTier": 4,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          },
          "PostMatchCsr": {
            "Value": 1063,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Platinum",
            "TierStart": 1050,
            "SubTier": 3,
            "NextTier": "Platinum",
            "NextTierStart": 1100,
            "NextSubTier": 4,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          }
        },
        "StatPerformances": {
          "Kills": {
            "Count": 12,
            "Expected": 10.022246124988976,
            "StdDev": 4.849186111057256
          },
          "Deaths": {
            "Count": 15,
            "Expected": 14.209475843196978,
            "StdDev": 4.495774138042733
          }
        },
        "TeamId": 1,
        "TeamMmrs": {
          "0": 1349.0048565602551,
          "1": 1265.0965428574646
        },
        "RankedRewards": null,
        "Counterfactuals": {
          "SelfCounterfactuals": {
            "Kills": 10.022246124988976,
            "Deaths": 14.209475843196978
          },
          "TierCounterfactuals": {
            "Bronze": {
              "Kills": -0.5955854742724225,
              "Deaths": 18.12466949970334
            },
            "Silver": {
              "Kills": 0.7612300081311131,
              "Deaths": 17.05641611631366
            },
            "Gold": {
              "Kills": 3.7458523105117645,
              "Deaths": 16.0052036406151
            },
            "Platinum": {
              "Kills": 7.7351175512391395,
              "Deaths": 14.873467143153261
            },
            "Diamond": {
              "Kills": 11.787431113608774,
              "Deaths": 13.673379279820528
            },
            "Onyx": {
              "Kills": 15.544530953081413,
              "Deaths": 12.477267418471937
            }
          }
        }
      }
    },
    {
      "Id": "xuid(2535416229856322)",
      "ResultCode": 0,
      "Result": {
        "TeamMmr": 1265.0965428574646,
        "RankRecap": {
          "PreMatchCsr": {
            "Value": 1351,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1350,
            "SubTier": 3,
            "NextTier": "Diamond",
            "NextTierStart": 1400,
            "NextSubTier": 4,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          },
          "PostMatchCsr": {
            "Value": 1344,
            "MeasurementMatchesRemaining": 0,
            "Tier": "Diamond",
            "TierStart": 1300,
            "SubTier": 2,
            "NextTier": "Diamond",
            "NextTierStart": 1350,
            "NextSubTier": 3,
            "InitialMeasurementMatches": 5,
            "DemotionProtectionMatchesRemaining": 0,
            "InitialDemotionProtectionMatches": 3
          }
        },
        "StatPerformances": {
          "Kills": {
            "Count": 15,
            "Expected": 13.200267448758046,
            "StdDev": 4.740528941980394
          },
          "Deaths": {
            "Count": 12,
            "Expected": 13.230745532444397,
            "StdDev": 4.511368417352668
          }
        },
        "TeamId": 1,
        "TeamMmrs": {
          "0": 1349.0048565602551,
          "1": 1265.0965428574646
        },
        "RankedRewards": null,
        "Counterfactuals": {
          "SelfCounterfactuals": {
            "Kills": 13.200267448758046,
            "Deaths": 13.230745532444397
          },
          "TierCounterfactuals": {
            "Bronze": {
              "Kills": -0.6478341550224597,
              "Deaths": 18.26340940599547
            },
            "Silver": {
              "Kills": 0.48021854711989787,
              "Deaths": 17.195269418132426
            },
            "Gold": {
              "Kills": 3.284238605051707,
              "Deaths": 16.144287772557522
            },
            "Platinum": {
              "Kills": 7.241731275464591,
              "Deaths": 15.013040121594427
            },
            "Diamond": {
              "Kills": 11.331212624614286,
              "Deaths": 13.813927330438453
            },
            "Onyx": {
              "Kills": 15.106385079413057,
              "Deaths": 12.61948879542619
            }
          }
        }
      }
    }
  ]
}
  ```
- **MatchId**: `90e0b3e4-b72f-48ce-9198-43c89f6814ef`


## Table: `PlaylistCSRSnapshots`

### Schema
```sql
CREATE TABLE PlaylistCSRSnapshots (

   ResponseBody TEXT,

   PlaylistId TEXT,

   PlaylistVersion TEXT,

   SnapshotTimestamp DATETIME,

   Value Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Value')) VIRTUAL

)
```

**Records: 16**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "Value": [
    {
      "Id": "xuid({YOUR_XUID})",
      "ResultCode": 0,
      "Result": {
        "Current": {
          "Value": 1020,
          "MeasurementMatchesRemaining": 0,
          "Tier": "Platinum",
          "TierStart": 1000,
          "SubTier": 2,
          "NextTier": "Platinum",
          "NextTierStart": 1050,
          "NextSubTier": 3,
          "InitialMeasurementMatches": 5,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 3
        },
        "SeasonMax": {
          "Value": 1090,
          "MeasurementMatchesRemaining": 0,
          "Tier": "Platinum",
          "TierStart": 1050,
          "SubTier": 3,
          "NextTier": "Platinum",
          "NextTierStart": 1100,
          "NextSubTier": 4,
          "InitialMeasurementMatches": 5,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 3
        },
        "AllTimeMax": {
          "Value": 1588,
          "MeasurementMatchesRemaining": 0,
          "Tier": "Onyx",
          "TierStart": 1500,
          "SubTier": 0,
          "NextTier": "Onyx",
          "NextTierStart": 1500,
          "NextSubTier": 0,
          "InitialMeasurementMatches": 5,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 3
        }
      }
    }
  ]
}
  ```
- **PlaylistId**: `edfef3ac-9cbe-4fa2-b949-8f29deafd483`
- **PlaylistVersion**: `37dd70c7-3ee7-4c87-b725-4b1a08d1b55d`
- **SnapshotTimestamp**: `2026-05-11T22:10:27.666+09:00`

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "Value": [
    {
      "Id": "xuid({YOUR_XUID})",
      "ResultCode": 0,
      "Result": {
        "Current": {
          "Value": 1083,
          "MeasurementMatchesRemaining": 0,
          "Tier": "Platinum",
          "TierStart": 1050,
          "SubTier": 3,
          "NextTier": "Platinum",
          "NextTierStart": 1100,
          "NextSubTier": 4,
          "InitialMeasurementMatches": 5,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 3
        },
        "SeasonMax": {
          "Value": 1083,
          "MeasurementMatchesRemaining": 0,
          "Tier": "Platinum",
          "TierStart": 1050,
          "SubTier": 3,
          "NextTier": "Platinum",
          "NextTierStart": 1100,
          "NextSubTier": 4,
          "InitialMeasurementMatches": 5,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 3
        },
        "AllTimeMax": {
          "Value": 1153,
          "MeasurementMatchesRemaining": 0,
          "Tier": "Platinum",
          "TierStart": 1150,
          "SubTier": 5,
          "NextTier": "Diamond",
          "NextTierStart": 1200,
          "NextSubTier": 0,
          "InitialMeasurementMatches": 5,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 3
        }
      }
    }
  ]
}
  ```
- **PlaylistId**: `fa5aa2a3-2428-4912-a023-e1eeea7b877c`
- **PlaylistVersion**: `771ce9f8-2a53-43cf-97c1-9ef71ee848da`
- **SnapshotTimestamp**: `2026-05-11T22:10:39.598+09:00`


## Table: `PlaylistMapModePairs`

### Schema
```sql
CREATE TABLE PlaylistMapModePairs (

	ResponseBody TEXT,

	CustomData Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CustomData')) VIRTUAL,

	Tags Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Tags')) VIRTUAL,

	MapLink Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.MapLink')) VIRTUAL,

	UgcGameVariantLink Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.UgcGameVariantLink')) VIRTUAL,

	AssetId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetId')) VIRTUAL,

	VersionId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionId')) VIRTUAL,

	PublicName Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublicName')) VIRTUAL,

	Description Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,

	Files Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Files')) VIRTUAL,

	Contributors Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Contributors')) VIRTUAL,

	AssetHome Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetHome')) VIRTUAL,

	AssetStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetStats')) VIRTUAL,

	InspectionResult Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InspectionResult')) VIRTUAL,

	CloneBehavior Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CloneBehavior')) VIRTUAL,

	"Order" Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Order')) VIRTUAL,

	PublishedDate Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublishedDate')) VIRTUAL,

	VersionNumber Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionNumber')) VIRTUAL,

	Admin Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Admin')) VIRTUAL

)
```

**Records: 465**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "CustomData": {},
  "Tags": [],
  "MapLink": {
    "AssetId": "654dff62-d618-496a-8914-06ab73d991e3",
    "VersionId": "87e7bd29-9914-48f3-81e0-38ad200e1e4e",
    "PublicName": "Interference",
    "Description": "Reimagination of the Halo 5's map The Rig with a snowy theme. Upscaled to accommodate Infinite's mechanics. It supports: Slayer, Strongholds and King of the Hill.",
    "Files": {
      "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/map/654dff62-d618-496a-8914-06ab73d991e3/87e7bd29-9914-48f3-81e0-38ad200e1e4e/",
      "FileRelativePaths": [
        "images/hero.jpg",
        "images/screenshot1.jpg",
        "images/screenshot2.jpg",
        "images/screenshot3.jpg",
        "images/thumbnail.jpg"
      ],
      "PrefixEndpoint": {
        "AuthorityId": "iUgcFiles",
        "Path": "/ugcstorage/map/654dff62-d618-496a-8914-06ab73d991e3/87e7bd29-9914-48f3-81e0-38ad200e1e4e/",
        "QueryString": null,
        "RetryPolicyId": "linearretry",
        "TopicName": "",
        "AcknowledgementTypeId": 0,
        "AuthenticationLifetimeExtensionSupported": false,
        "ClearanceAware": false
      }
    },
    "Contributors": [
      "xuid(2814673621658978)",
      "xuid(2533274885566464)",
      "xuid(2535434382229776)",
      "xuid(2535431248047890)",
      "xuid(2533274888129123)",
      "xuid(2535409849610595)",
      "xuid(2533274798663195)",
      "xuid(2533274955934650)",
      "xuid(2659938529929265)"
    ],
    "AssetHome": 1,
    "AssetStats": {
      "PlaysRecent": 3670,
      "PlaysAllTime": 3645172,
      "Favorites": 4503,
      "Likes": 0,
      "Bookmarks": 0,
      "ParentAssetCount": 20,
      "AverageRating": 3.902350813743219,
      "NumberOfRatings": 553
    },
    "InspectionResult": 0,
    "CloneBehavior": 2,
    "Order": 0,
    "PublishedDate": {
      "ISO8601Date": "2021-11-15T12:00:00Z"
    },
    "VersionNumber": 5,
    "Admin": "xuid(2533274885566464)",
    "DisplayOwnerOverride": "xuid(2533274885566464)"
  },
  "UgcGameVariantLink": {
    "AssetId": "c2d20d44-8606-4669-b894-afae15b3524f",
    "VersionId": "0091d411-f90d-44a7-aac3-ccc7ff2b131f",
    "PublicName": "Ranked:Slayer",
    "Description": "Bandit Evo loadouts, Friendly-Fire enabled, Motion Tracker disabled. Slay the enemy team.",
    "Files": {
      "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/ugcgamevariant/c2d20d44-8606-4669-b894-afae15b3524f/0091d411-f90d-44a7-aac3-ccc7ff2b131f/",
      "FileRelativePaths": [
        "images/hero.png",
        "images/screenshot1.Png",
        "images/screenshot1.png",
        "images/screenshot2.Png",
        "images/screenshot2.png",
        "images/screenshot3.Png",
        "images/screenshot3.png",
        "images/thumbnail.png"
      ],
      "PrefixEndpoint": {
        "AuthorityId": "iUgcFiles",
        "Path": "/ugcstorage/ugcgamevariant/c2d20d44-8606-4669-b894-afae15b3524f/0091d411-f90d-44a7-aac3-ccc7ff2b131f/",
        "QueryString": null,
        "RetryPolicyId": "linearretry",
        "TopicName": "",
        "AcknowledgementTypeId": 0,
        "AuthenticationLifetimeExtensionSupported": false,
        "ClearanceAware": false
      }
    },
    "Contributors": [],
    "AssetHome": 1,
    "AssetStats": {
      "PlaysRecent": 40929,
      "PlaysAllTime": 38606845,
      "Favorites": 52971,
      "Likes": 0,
      "Bookmarks": 0,
      "ParentAssetCount": 145,
      "AverageRating": 3.822296280369813,
      "NumberOfRatings": 27906
    },
    "InspectionResult": 0,
    "CloneBehavior": 0,
    "Order": 0,
    "PublishedDate": {
      "ISO8601Date": "2021-11-15T12:00:00Z"
    },
    "VersionNumber": 8,
    "Admin": "aaid(5c7909e9-3620-4920-8abf-f18cfb4333b6)",
    "DisplayOwnerOverride": ""
  },
  "AssetId": "6d60d1d2-cc97-4b4e-88a4-9755e110e3c3",
  "VersionId": "b0440694-46e4-4981-9431-bdf8b00e948e",
  "PublicName": "Ranked:Slayer on Interference",
  "Description": "",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/6d60d1d2-cc97-4b4e-88a4-9755e110e3c3/b0440694-46e4-4981-9431-bdf8b00e948e/",
    "FileRelativePaths": [],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/mapmodepair/6d60d1d2-cc97-4b4e-88a4-9755e110e3c3/b0440694-46e4-4981-9431-bdf8b00e948e/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [],
  "AssetHome": 1,
  "AssetStats": {
    "PlaysRecent": 2306,
    "PlaysAllTime": 1063976,
    "Favorites": 0,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 1,
    "AverageRating": 0.0,
    "NumberOfRatings": 0
  },
  "InspectionResult": 0,
  "CloneBehavior": 0,
  "Order": 0,
  "PublishedDate": null,
  "VersionNumber": 10,
  "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.7c4ee670-d225-4aaa-aa11-ad7a600b130a)",
  "DisplayOwnerOverride": ""
}
  ```

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "CustomData": {},
  "Tags": [],
  "MapLink": {
    "AssetId": "1a6cfc2e-ec86-48e1-9464-1ce1bff6ed48",
    "VersionId": "3a382104-9b89-4e6e-aa18-0affaa98f478",
    "PublicName": "Lattice - Ranked",
    "Description": "This abandoned hydroelectric facility holds secrets once buried under the ice.",
    "Files": {
      "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/map/1a6cfc2e-ec86-48e1-9464-1ce1bff6ed48/3a382104-9b89-4e6e-aa18-0affaa98f478/",
      "FileRelativePaths": [
        "images/hero.jpg",
        "images/screenshot1.jpg",
        "images/screenshot2.jpg",
        "images/screenshot3.jpg",
        "images/thumbnail.jpg"
      ],
      "PrefixEndpoint": {
        "AuthorityId": "iUgcFiles",
        "Path": "/ugcstorage/map/1a6cfc2e-ec86-48e1-9464-1ce1bff6ed48/3a382104-9b89-4e6e-aa18-0affaa98f478/",
        "QueryString": null,
        "RetryPolicyId": "linearretry",
        "TopicName": "",
        "AcknowledgementTypeId": 0,
        "AuthenticationLifetimeExtensionSupported": false,
        "ClearanceAware": false
      }
    },
    "Contributors": [
      "xuid(2814640426484785)",
      "xuid(2814673621658978)",
      "xuid(2814620018427310)"
    ],
    "AssetHome": 1,
    "AssetStats": {
      "PlaysRecent": 10527,
      "PlaysAllTime": 620420,
      "Favorites": 5009,
      "Likes": 0,
      "Bookmarks": 0,
      "ParentAssetCount": 17,
      "AverageRating": 3.393939393939394,
      "NumberOfRatings": 165
    },
    "InspectionResult": 0,
    "CloneBehavior": 0,
    "Order": 0,
    "PublishedDate": {
      "ISO8601Date": "2021-11-15T12:00:00Z"
    },
    "VersionNumber": 4,
    "Admin": "xuid(2814673621658978)",
    "DisplayOwnerOverride": ""
  },
  "UgcGameVariantLink": {
    "AssetId": "751bcc9d-aace-45a1-8d71-358f0bc89f7e",
    "VersionId": "227d4ffc-d67f-449a-8315-a1f82854d2ed",
    "PublicName": "Ranked:Oddball",
    "Description": "Bandit Evo loadouts, Friendly-Fire enabled, Motion Tracker disabled. Hold the flaming skull.",
    "Files": {
      "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/ugcgamevariant/751bcc9d-aace-45a1-8d71-358f0bc89f7e/227d4ffc-d67f-449a-8315-a1f82854d2ed/",
      "FileRelativePaths": [
        "images/hero.png",
        "images/screenshot1.png",
        "images/screenshot2.png",
        "images/screenshot3.png",
        "images/thumbnail.png"
      ],
      "PrefixEndpoint": {
        "AuthorityId": "iUgcFiles",
        "Path": "/ugcstorage/ugcgamevariant/751bcc9d-aace-45a1-8d71-358f0bc89f7e/227d4ffc-d67f-449a-8315-a1f82854d2ed/",
        "QueryString": null,
        "RetryPolicyId": "linearretry",
        "TopicName": "",
        "AcknowledgementTypeId": 0,
        "AuthenticationLifetimeExtensionSupported": false,
        "ClearanceAware": false
      }
    },
    "Contributors": [],
    "AssetHome": 1,
    "AssetStats": {
      "PlaysRecent": 15236,
      "PlaysAllTime": 17684575,
      "Favorites": 24267,
      "Likes": 0,
      "Bookmarks": 0,
      "ParentAssetCount": 68,
      "AverageRating": 2.4540666011963217,
      "NumberOfRatings": 22402
    },
    "InspectionResult": 0,
    "CloneBehavior": 0,
    "Order": 0,
    "PublishedDate": {
      "ISO8601Date": "2021-11-15T12:00:00Z"
    },
    "VersionNumber": 8,
    "Admin": "aaid(5c7909e9-3620-4920-8abf-f18cfb4333b6)",
    "DisplayOwnerOverride": ""
  },
  "AssetId": "4aa35370-79dd-4e34-891d-710bcdfa226a",
  "VersionId": "453c720a-4ce5-4f8b-b03d-9fe2759f4148",
  "PublicName": "Ranked:Oddball on Lattice - Ranked",
  "Description": "",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/4aa35370-79dd-4e34-891d-710bcdfa226a/453c720a-4ce5-4f8b-b03d-9fe2759f4148/",
    "FileRelativePaths": [],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/mapmodepair/4aa35370-79dd-4e34-891d-710bcdfa226a/453c720a-4ce5-4f8b-b03d-9fe2759f4148/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [],
  "AssetHome": 1,
  "AssetStats": {
    "PlaysRecent": 3158,
    "PlaysAllTime": 135732,
    "Favorites": 0,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 1,
    "AverageRating": 0.0,
    "NumberOfRatings": 0
  },
  "InspectionResult": 0,
  "CloneBehavior": 0,
  "Order": 0,
  "PublishedDate": null,
  "VersionNumber": 5,
  "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
  "DisplayOwnerOverride": ""
}
  ```


## Table: `Playlists`

### Schema
```sql
CREATE TABLE Playlists (

	ResponseBody TEXT,

	CustomData Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CustomData')) VIRTUAL,

	Tags Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Tags')) VIRTUAL,

	RotationEntries Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.RotationEntries')) VIRTUAL,

	AssetId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetId')) VIRTUAL,

	VersionId Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionId')) VIRTUAL,

	PublicName Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublicName')) VIRTUAL,

	Description Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Description')) VIRTUAL,

	Files Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Files')) VIRTUAL,

	Contributors Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Contributors')) VIRTUAL,

	AssetHome Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetHome')) VIRTUAL,

	AssetStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.AssetStats')) VIRTUAL,

	InspectionResult Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InspectionResult')) VIRTUAL,

	CloneBehavior Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CloneBehavior')) VIRTUAL,

	"Order" Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Order')) VIRTUAL,

	PublishedDate Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.PublishedDate')) VIRTUAL,

	VersionNumber Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.VersionNumber')) VIRTUAL,

	Admin Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Admin')) VIRTUAL

)
```

**Records: 28**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "CustomData": {
    "PlaylistEntries": [
      {
        "MapModePairAssetId": "fbd9b00d-f937-44f2-b94f-a988ec847ad5",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "3399922a-716f-448b-8208-114ff048def7",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "f250c4ba-b4fe-4a00-b456-257243827582",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "10ef8b24-22b8-410b-a1b9-da723a380e63",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "678d3617-b75f-4fa1-8ada-26e0a0c69c73",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "709b596a-515d-4557-8184-a57bf55eb6b6",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "429fb8ca-8ab3-400a-873f-d39f2c7489bb",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "d7bade10-0473-432b-bffc-6f2f83015223",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "2548b22a-33fe-4567-95c9-1ba14daa822e",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "0e402517-fd04-4471-a8dc-8d56c3887fba",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "1dc96cdb-3cb9-4ca0-b6e5-6de655e4e887",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "6592f3fe-622a-4b34-bf47-2d55bd9076c8",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "81658371-3f41-451f-97ae-63a0306b7e69",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "1548b550-7b2e-4df6-94b1-36f9940e4a69",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "e3b702ab-718a-41c9-9a8d-487857e9fcfc",
        "Metadata": {
          "Weight": 175.0
        }
      },
      {
        "MapModePairAssetId": "06dd1b60-9e93-46b0-bcca-072add89aece",
        "Metadata": {
          "Weight": 175.0
        }
      },
      {
        "MapModePairAssetId": "00f71772-fa4d-4386-b15e-d89b4a1ce5fd",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "3435b323-a49e-4229-b4f7-8c63487fa682",
        "Metadata": {
          "Weight": 70.0
        }
      },
      {
        "MapModePairAssetId": "97364ca4-388c-480b-9f9e-4ccbfabe054d",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "73c99fa2-6937-4077-ac58-c8dbd2f9bfbc",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "2559206b-3480-4f1c-b8f0-473bbcb5de92",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "100088fe-d17d-4798-b76f-aba901130298",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "58ebb017-f2ac-4788-b07e-a49364819d7f",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "5280d785-d035-4ec9-9cb1-9b95b03d852e",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "7925ce26-78be-44e5-a0f0-da366e343955",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "f13f4ef7-5972-4138-ae59-ef9b7272d309",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "31ea4f3c-b9bb-4426-a9ff-a84e668c2f93",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "45f3f888-d963-4119-ba4b-fccab517e838",
        "Metadata": {
          "Weight": 70.0
        }
      },
      {
        "MapModePairAssetId": "ec61aa00-7457-4be4-aaf9-eb7efb787f07",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "6d60d1d2-cc97-4b4e-88a4-9755e110e3c3",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "1a8b79e1-3153-446e-a099-3926af553db5",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "79232d2a-1a60-47f5-bcc0-f62a1a7a4031",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "87d76a14-42f9-408c-b848-c73ca5db7f2b",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "f1e29187-db75-43cd-869e-6ea61fc61b31",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "25cd7214-819e-47c0-ba89-42c9b82cc852",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "585adae4-3988-4052-8141-8756988719e3",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "e5be97a1-fa5a-42f0-bce7-697d06399efa",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "81b7e671-9d4d-436e-858d-b87ccce8d5bb",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "5cb82a78-fbf1-4dd6-bfe6-be9212066a69",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "0aab5cd3-c09f-40d1-9031-af4ec163613b",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "9010dcab-ea1d-4a93-930b-972a52a074c4",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "4ea10ed0-2e34-4c96-9545-b36f82fa0846",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "ca8d534c-9194-42d9-844a-d09175a28504",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "2fa5d8f0-2e0c-42d5-a089-1594dc454308",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "b1dabcb3-d7ab-468c-a48a-01ec747a1f83",
        "Metadata": {
          "Weight": 90.0
        }
      }
    ],
    "Strategy": 0,
    "MinTeams": 2,
    "MinTeamSize": 4,
    "MaxTeams": 2,
    "MaxTeamSize": 4,
    "MaxTeamImbalance": 0,
    "MaxSplitscreenPlayersAllowed": 4,
    "AllowFriendJoinInProgress": false,
    "AllowMatchmakingJoinInProgress": false,
    "AllowBotJoinInProgress": false,
    "ExitExperienceDurationSec": 30,
    "FireteamLeaderKickAllowed": false,
    "DisableMidgameChat": false,
    "AllowedDeviceInputs": [
      0
    ],
    "BotDifficulty": 3,
    "MinFireteamSize": 1,
    "MaxFireteamSize": 4
  },
  "Tags": [],
  "RotationEntries": [
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "31ea4f3c-b9bb-4426-a9ff-a84e668c2f93",
      "VersionId": "cd9a712e-557b-4c59-a574-3e370f57a755",
      "PublicName": "Ranked:Slayer on Streets - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/31ea4f3c-b9bb-4426-a9ff-a84e668c2f93/cd9a712e-557b-4c59-a574-3e370f57a755/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/31ea4f3c-b9bb-4426-a9ff-a84e668c2f93/cd9a712e-557b-4c59-a574-3e370f57a755/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2324,
        "PlaysAllTime": 1100071,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 13,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.7c4ee670-d225-4aaa-aa11-ad7a600b130a)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "1a8b79e1-3153-446e-a099-3926af553db5",
      "VersionId": "92466efd-744b-4d3e-a34a-99a08dcbffb4",
      "PublicName": "Ranked:Slayer on Empyrean - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/1a8b79e1-3153-446e-a099-3926af553db5/92466efd-744b-4d3e-a34a-99a08dcbffb4/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/1a8b79e1-3153-446e-a099-3926af553db5/92466efd-744b-4d3e-a34a-99a08dcbffb4/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2317,
        "PlaysAllTime": 1033907,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 8,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "6d60d1d2-cc97-4b4e-88a4-9755e110e3c3",
      "VersionId": "b0440694-46e4-4981-9431-bdf8b00e948e",
      "PublicName": "Ranked:Slayer on Interference",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/6d60d1d2-cc97-4b4e-88a4-9755e110e3c3/b0440694-46e4-4981-9431-bdf8b00e948e/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/6d60d1d2-cc97-4b4e-88a4-9755e110e3c3/b0440694-46e4-4981-9431-bdf8b00e948e/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2306,
        "PlaysAllTime": 1063976,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 10,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.7c4ee670-d225-4aaa-aa11-ad7a600b130a)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "585adae4-3988-4052-8141-8756988719e3",
      "VersionId": "6a8aa195-e47c-4e61-a5f0-c481283154b7",
      "PublicName": "Ranked:Slayer on Origin - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/585adae4-3988-4052-8141-8756988719e3/6a8aa195-e47c-4e61-a5f0-c481283154b7/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/585adae4-3988-4052-8141-8756988719e3/6a8aa195-e47c-4e61-a5f0-c481283154b7/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2268,
        "PlaysAllTime": 757179,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 6,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 100.0
      },
      "AssetId": "5280d785-d035-4ec9-9cb1-9b95b03d852e",
      "VersionId": "8a8a4305-a56b-43cf-ad07-f1f04f652ae6",
      "PublicName": "Ranked:Slayer on Live Fire - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/5280d785-d035-4ec9-9cb1-9b95b03d852e/8a8a4305-a56b-43cf-ad07-f1f04f652ae6/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/5280d785-d035-4ec9-9cb1-9b95b03d852e/8a8a4305-a56b-43cf-ad07-f1f04f652ae6/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2503,
        "PlaysAllTime": 1300461,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 13,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.7c4ee670-d225-4aaa-aa11-ad7a600b130a)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "f13f4ef7-5972-4138-ae59-ef9b7272d309",
      "VersionId": "a2e548bb-c604-4504-9e9a-23abe4c2fab4",
      "PublicName": "Ranked:Slayer on Solitude - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/f13f4ef7-5972-4138-ae59-ef9b7272d309/a2e548bb-c604-4504-9e9a-23abe4c2fab4/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/f13f4ef7-5972-4138-ae59-ef9b7272d309/a2e548bb-c604-4504-9e9a-23abe4c2fab4/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2285,
        "PlaysAllTime": 1090929,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 13,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.7c4ee670-d225-4aaa-aa11-ad7a600b130a)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "2fa5d8f0-2e0c-42d5-a089-1594dc454308",
      "VersionId": "71798da4-c4b6-40fe-870d-f9b8380679f9",
      "PublicName": "Ranked:Slayer on Lattice - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/2fa5d8f0-2e0c-42d5-a089-1594dc454308/71798da4-c4b6-40fe-870d-f9b8380679f9/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/2fa5d8f0-2e0c-42d5-a089-1594dc454308/71798da4-c4b6-40fe-870d-f9b8380679f9/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2303,
        "PlaysAllTime": 63417,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 1,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "ca8d534c-9194-42d9-844a-d09175a28504",
      "VersionId": "aeef042e-40f3-476f-9a9e-20e2079d9896",
      "PublicName": "Ranked:Slayer on Vacancy - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/ca8d534c-9194-42d9-844a-d09175a28504/aeef042e-40f3-476f-9a9e-20e2079d9896/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/ca8d534c-9194-42d9-844a-d09175a28504/aeef042e-40f3-476f-9a9e-20e2079d9896/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2293,
        "PlaysAllTime": 63288,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 1,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "00f71772-fa4d-4386-b15e-d89b4a1ce5fd",
      "VersionId": "1afae189-c8f1-46a7-babf-9268a0ae7f38",
      "PublicName": "Ranked:Slayer on Aquarius - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/00f71772-fa4d-4386-b15e-d89b4a1ce5fd/1afae189-c8f1-46a7-babf-9268a0ae7f38/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/00f71772-fa4d-4386-b15e-d89b4a1ce5fd/1afae189-c8f1-46a7-babf-9268a0ae7f38/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2326,
        "PlaysAllTime": 1074829,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 13,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.7c4ee670-d225-4aaa-aa11-ad7a600b130a)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "7925ce26-78be-44e5-a0f0-da366e343955",
      "VersionId": "0135d068-c44e-4c27-b487-7f5dea665757",
      "PublicName": "Ranked:Slayer on Recharge - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/7925ce26-78be-44e5-a0f0-da366e343955/0135d068-c44e-4c27-b487-7f5dea665757/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/7925ce26-78be-44e5-a0f0-da366e343955/0135d068-c44e-4c27-b487-7f5dea665757/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2274,
        "PlaysAllTime": 1107720,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 13,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.7c4ee670-d225-4aaa-aa11-ad7a600b130a)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 90.0
      },
      "AssetId": "b1dabcb3-d7ab-468c-a48a-01ec747a1f83",
      "VersionId": "51fcf4b3-3b9c-4ba2-a552-8213b9e7b9d7",
      "PublicName": "Ranked:Slayer on Serenity - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/b1dabcb3-d7ab-468c-a48a-01ec747a1f83/51fcf4b3-3b9c-4ba2-a552-8213b9e7b9d7/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/b1dabcb3-d7ab-468c-a48a-01ec747a1f83/51fcf4b3-3b9c-4ba2-a552-8213b9e7b9d7/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2267,
        "PlaysAllTime": 63643,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 1,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    }
  ],
  "AssetId": "dcb2e24e-05fb-4390-8076-32a0cdb4326e",
  "VersionId": "1f86eb44-cf6d-4969-950c-bebc8ce04407",
  "PublicName": "Ranked Slayer",
  "Description": "[RANKED] [4v4] Slay the enemy team. Bandit Evo loadout. Motion tracker and Friendly Fire are enabled.",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/playlist/dcb2e24e-05fb-4390-8076-32a0cdb4326e/1f86eb44-cf6d-4969-950c-bebc8ce04407/",
    "FileRelativePaths": [
      "images/hero.jpg",
      "images/screenshot1.jpg",
      "images/thumbnail.jpg"
    ],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/playlist/dcb2e24e-05fb-4390-8076-32a0cdb4326e/1f86eb44-cf6d-4969-950c-bebc8ce04407/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [],
  "AssetHome": 1,
  "AssetStats": {
    "PlaysRecent": 0,
    "PlaysAllTime": 0,
    "Favorites": 0,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 11,
    "AverageRating": 0.0,
    "NumberOfRatings": 0
  },
  "InspectionResult": 0,
  "CloneBehavior": 0,
  "Order": 0,
  "PublishedDate": null,
  "VersionNumber": 22,
  "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
  "DisplayOwnerOverride": ""
}
  ```

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "CustomData": {
    "PlaylistEntries": [
      {
        "MapModePairAssetId": "5f4fedf5-fcb5-4984-aba7-fc82ec6ebb85",
        "Metadata": {
          "Weight": 1.0
        }
      },
      {
        "MapModePairAssetId": "f5f1e083-0739-4077-96ea-1de428de2249",
        "Metadata": {
          "Weight": 65.0
        }
      },
      {
        "MapModePairAssetId": "2c6df2e1-b2d0-4572-b44e-8352aa3b1d77",
        "Metadata": {
          "Weight": 1.0
        }
      },
      {
        "MapModePairAssetId": "4376e40e-8841-4957-8596-506a626a2a96",
        "Metadata": {
          "Weight": 65.0
        }
      },
      {
        "MapModePairAssetId": "892a4ca3-a682-40d6-850e-2addb57b0473",
        "Metadata": {
          "Weight": 65.0
        }
      },
      {
        "MapModePairAssetId": "dd6688c8-1dce-4772-a51d-cbf0301b5f1c",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "6fd98bba-096f-465a-86b4-38b7ff1c3726",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "53755e77-95ea-4ec1-8585-6f072b55346b",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "9cdc376a-dcc2-42c1-bc91-df5fb75e6da9",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "40b19c6b-0355-454e-98b4-21f07771e3ab",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "ca4ffa61-a7fe-4e73-9d32-2b77c6ef8f03",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "8b810aa7-ca65-43cb-9037-793b783110c5",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "3eeeba49-302d-4fef-af88-46b266bceecd",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "183778b7-8e76-4932-894e-b39421f650da",
        "Metadata": {
          "Weight": 90.0
        }
      },
      {
        "MapModePairAssetId": "1a5296b6-9e9f-4bd0-ad61-cd112f38901b",
        "Metadata": {
          "Weight": 145.0
        }
      },
      {
        "MapModePairAssetId": "9f5c682e-e985-4fbb-b5fc-05f091bd75e5",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "d3656a79-c835-49db-aa10-5d7ccf5fca5e",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "e14c56b1-5484-4b25-ad5c-578946f7173b",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "ac6a7411-b0df-4f9d-8cf5-3263fdef736d",
        "Metadata": {
          "Weight": 65.0
        }
      },
      {
        "MapModePairAssetId": "cf8f5925-e6e3-413d-882b-c5473b9d589d",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "ee5adc4a-bc37-4e76-872c-8c2688d33dac",
        "Metadata": {
          "Weight": 115.0
        }
      },
      {
        "MapModePairAssetId": "641da151-969c-441f-b38b-b7f04f22e5a9",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "979ec64e-b35d-4f01-88ea-fc4123c20f26",
        "Metadata": {
          "Weight": 140.0
        }
      },
      {
        "MapModePairAssetId": "38d03b76-e614-4252-b31d-eb85b8bef173",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "bd4056de-a317-4899-ab21-125b29762f4b",
        "Metadata": {
          "Weight": 140.0
        }
      },
      {
        "MapModePairAssetId": "013e4758-e1bc-4ac9-abd3-79f6e0e8bbe9",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "d380aaeb-0877-404b-bf8c-2336ed99d62b",
        "Metadata": {
          "Weight": 140.0
        }
      },
      {
        "MapModePairAssetId": "b96e888b-2f33-453b-a198-25dcaee5d546",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "4d1cb40b-05cb-4330-a37a-d8cb64db384f",
        "Metadata": {
          "Weight": 115.0
        }
      },
      {
        "MapModePairAssetId": "a062e020-e143-4c9c-8037-864575de20b5",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "0abd3c32-308f-4f7c-9920-62c8cc2d5ced",
        "Metadata": {
          "Weight": 155.0
        }
      },
      {
        "MapModePairAssetId": "a3cf7e98-111c-4c85-9f24-98c3cc549185",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "a2baf25d-b19b-4ec2-94c6-430822e50621",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "69d25f16-bc62-4d58-baf7-6210f65461f3",
        "Metadata": {
          "Weight": 75.0
        }
      },
      {
        "MapModePairAssetId": "9664fda6-1ca7-4c52-a236-20534d784e79",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "985ed5c0-5dce-4d6c-a892-d85536c2c10c",
        "Metadata": {
          "Weight": 55.0
        }
      },
      {
        "MapModePairAssetId": "cd0bed8a-2566-403c-a635-6807e5789599",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "ba7af0b3-5b8e-4f58-9b1c-41ba1bb51ced",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "030c62b3-95e7-44f0-9a8e-613366697bcb",
        "Metadata": {
          "Weight": 150.0
        }
      },
      {
        "MapModePairAssetId": "dc9f1df9-4496-4315-9976-e102d2d37387",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "ad1ec6fb-6e43-499a-a0d5-9f82663c0b27",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "baf39b25-1993-417a-9de6-fa33fcf7cf5e",
        "Metadata": {
          "Weight": 55.0
        }
      },
      {
        "MapModePairAssetId": "002875a0-9832-4924-ad2f-af598670c489",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "8661ecfd-e9cc-4eb1-af10-fab4a25e1e03",
        "Metadata": {
          "Weight": 75.0
        }
      },
      {
        "MapModePairAssetId": "ab755f1b-d1d8-4f74-a6d3-c5715ffd021b",
        "Metadata": {
          "Weight": 140.0
        }
      },
      {
        "MapModePairAssetId": "81ae1552-ffe5-4ff1-934b-251d64920111",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "cb3fb4da-75e5-4e51-aa65-b7476b9bb645",
        "Metadata": {
          "Weight": 75.0
        }
      },
      {
        "MapModePairAssetId": "580b9525-3dcb-4c15-bc7e-8adb634cfe71",
        "Metadata": {
          "Weight": 165.0
        }
      },
      {
        "MapModePairAssetId": "284dfe3e-a392-4c73-acee-fbc274399c2f",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "d1c49596-2d2a-457f-b687-2f9c9cb7dcef",
        "Metadata": {
          "Weight": 75.0
        }
      },
      {
        "MapModePairAssetId": "26ec012b-7d63-4bc4-a06d-ac1b7c420290",
        "Metadata": {
          "Weight": 75.0
        }
      },
      {
        "MapModePairAssetId": "5a845594-266d-48b1-9737-9ff2c8e933d9",
        "Metadata": {
          "Weight": 75.0
        }
      },
      {
        "MapModePairAssetId": "a61ba59b-054d-4363-ad61-940a5487e987",
        "Metadata": {
          "Weight": 75.0
        }
      },
      {
        "MapModePairAssetId": "48cfaf0f-0d22-44d7-b6e4-8ac340f1fa98",
        "Metadata": {
          "Weight": 75.0
        }
      },
      {
        "MapModePairAssetId": "a9d28865-9307-4ebe-b8fd-ea765a6db0be",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "381c8484-c9a8-4dc7-a71f-4e5989953f78",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "21b64eff-a901-4f50-9a99-9f7e461867e3",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "ce2adb1e-e06d-4e0f-b211-e9183845ac15",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "9f4a6ed4-5bf1-4590-9710-a3bfe36e5eae",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "3d123550-d421-4699-9235-99c613b43761",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "5cacdf11-f159-4eb8-91d9-b78d49c902b4",
        "Metadata": {
          "Weight": 155.0
        }
      },
      {
        "MapModePairAssetId": "b087baf3-f365-4d67-9126-dc4e26738e03",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "8c2d4991-a794-4ef4-9fde-391126152571",
        "Metadata": {
          "Weight": 140.0
        }
      },
      {
        "MapModePairAssetId": "f6a493f5-bedc-415d-a286-411b4793e520",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "b2c6a00e-c729-41f2-a690-fb8747b07fad",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "acc15257-e722-4d5c-943c-d7e4b8d16877",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "f005089e-60bc-466d-a536-b8c3d5e67928",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "acd7495e-d14f-4d1a-ac1f-ec546b3b1034",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "07518ed3-d120-4797-9729-6862cdd7072e",
        "Metadata": {
          "Weight": 155.0
        }
      },
      {
        "MapModePairAssetId": "ca847212-c0d0-4992-90c7-01c244c9a4fd",
        "Metadata": {
          "Weight": 155.0
        }
      },
      {
        "MapModePairAssetId": "e622e71d-9f6e-456b-b66e-548eecaf1459",
        "Metadata": {
          "Weight": 155.0
        }
      },
      {
        "MapModePairAssetId": "c6ae68b2-b067-4d49-93c6-65016e9c2330",
        "Metadata": {
          "Weight": 75.0
        }
      },
      {
        "MapModePairAssetId": "8ca490e9-c311-438a-82e1-737837f048e3",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "2a009ae4-1a8f-4f1a-8bd9-b0b15a09771b",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "2ccfc607-0eb5-43d1-a4db-ddeca494eac8",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "fbbfaff7-4272-4c8f-b8b1-9f83022ef4a3",
        "Metadata": {
          "Weight": 170.0
        }
      },
      {
        "MapModePairAssetId": "8f17df0d-deed-471b-82a9-8c4d0ad301a0",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "5a0f913a-5c65-4c2e-9c9c-a087f9a06d17",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "5fddf42a-2c96-4d6d-8107-1afa3b98881c",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "8491648c-f836-444f-bbc7-336852da7cd3",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "4e51d575-6281-46be-b557-97263a988b71",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "5286aa15-6381-418b-8b0a-c4da1c5cff5b",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "a49fe1f4-cea3-4dcd-8a52-08e73eeb191b",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "38fbdaad-7576-478e-9e29-1685e8bc3d82",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "c5bde97a-a3ef-4f4d-9a20-865930d8ccdd",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "6452a24a-b3c1-462f-a85d-4c42f7260272",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "190050e7-c1d1-4651-8ac9-9b530e9dd85b",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "e0860dcb-a40f-4318-ae33-4c73fa168cec",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "23da6ab8-6b9e-44a1-9d94-1c1865405c29",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "36d43c86-3118-4837-8d91-1ea77a987003",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "a7e8a1f5-f986-476a-82d4-0ee78a35a4a0",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "c5419548-ba26-41b1-af8e-e0b363e73f3d",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "26ecf6a9-12d1-4b94-8391-3aa39da84bb0",
        "Metadata": {
          "Weight": 105.0
        }
      },
      {
        "MapModePairAssetId": "68afdc68-ebe8-4e6e-8307-91934288033f",
        "Metadata": {
          "Weight": 170.0
        }
      },
      {
        "MapModePairAssetId": "e1a3af1e-7d82-498d-ae07-08e269073cd8",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "a3147590-d787-4b54-bc9a-c43a20b5ea7f",
        "Metadata": {
          "Weight": 170.0
        }
      },
      {
        "MapModePairAssetId": "64cce7ac-f026-4027-8db2-6a2b1b2f16b0",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "fa66bdcb-599d-4f14-9a58-7a1d13fc94a4",
        "Metadata": {
          "Weight": 165.0
        }
      },
      {
        "MapModePairAssetId": "90d835f8-f164-4427-a65b-9449a09f8de5",
        "Metadata": {
          "Weight": 165.0
        }
      },
      {
        "MapModePairAssetId": "0b8b3533-19ca-41f3-babb-0c9efe212325",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "40caf315-b372-44dd-af6a-c518e4c2a9a5",
        "Metadata": {
          "Weight": 120.0
        }
      },
      {
        "MapModePairAssetId": "81b9a6dc-02c2-4cc1-99f2-bd61064f4896",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "67550876-ef7c-46d6-9f6c-b4aa5f1ec9de",
        "Metadata": {
          "Weight": 160.0
        }
      },
      {
        "MapModePairAssetId": "a896f5c1-8322-45e7-8e25-677d8b7ed6fe",
        "Metadata": {
          "Weight": 165.0
        }
      },
      {
        "MapModePairAssetId": "271211bd-6410-4602-bfdb-4e14bc3aae06",
        "Metadata": {
          "Weight": 95.0
        }
      },
      {
        "MapModePairAssetId": "006e1d31-a5c3-4478-941f-8b14d73bf6f9",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "978ea5a9-f681-4b24-a925-6b99682e23d0",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "af23db65-41d1-40d0-8403-c1224114b46f",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "47845ea6-d4a8-438a-a820-1823e8132e74",
        "Metadata": {
          "Weight": 185.0
        }
      },
      {
        "MapModePairAssetId": "0ecc4c76-6a32-4d33-9fcb-2431e5543cd1",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "48deabd2-a32f-4516-9dc8-896ea0bd745f",
        "Metadata": {
          "Weight": 125.0
        }
      },
      {
        "MapModePairAssetId": "471b2e55-175b-4391-b694-6a4ae1f0a630",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "bbdbc179-374e-49fc-b96d-96ff685e46de",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "63c58031-facb-430d-bede-e4287f428c9c",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "4b334710-fc13-48d2-9876-104981224116",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "693aae7f-b3c1-4a7e-af28-a79a409b2a77",
        "Metadata": {
          "Weight": 305.0
        }
      },
      {
        "MapModePairAssetId": "7617463b-e347-4b22-932d-3336005700b4",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "86a76c53-336e-48d1-a59c-3565edc54c5c",
        "Metadata": {
          "Weight": 65.0
        }
      },
      {
        "MapModePairAssetId": "73de9756-2230-48ab-861e-8088fc527458",
        "Metadata": {
          "Weight": 65.0
        }
      },
      {
        "MapModePairAssetId": "26be7698-f41d-4c7c-b881-de072d2e572a",
        "Metadata": {
          "Weight": 65.0
        }
      },
      {
        "MapModePairAssetId": "e8c81bf4-aca2-4448-b697-4489db619c17",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "77919d2f-7ad7-417a-9421-476cd7f9a3b5",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "704c4733-657e-4a91-819c-47714d58d402",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "b8d8b03e-a53b-46b7-af58-4c0a704b2ef7",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "3125f6e8-07fb-45ff-8256-b1d69aae5ec0",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "08a7cc1d-1d6a-4ffe-bd4d-febe5aef183a",
        "Metadata": {
          "Weight": 195.0
        }
      },
      {
        "MapModePairAssetId": "2f71d2b7-8f99-4359-a50d-319f25d10a43",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "ddd829a0-f79c-4ad5-a3bb-162b00d75629",
        "Metadata": {
          "Weight": 40.0
        }
      },
      {
        "MapModePairAssetId": "b8a0efcd-a06e-4fa1-a792-32865582ea4c",
        "Metadata": {
          "Weight": 200.0
        }
      },
      {
        "MapModePairAssetId": "a39b04bf-9c4a-42f0-8b30-81acdc3e1e83",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "c43795d6-c87d-433b-9735-ed3cf4abbc14",
        "Metadata": {
          "Weight": 40.0
        }
      },
      {
        "MapModePairAssetId": "2bb084c2-a047-4fe9-9023-4100cbe6860d",
        "Metadata": {
          "Weight": 70.0
        }
      },
      {
        "MapModePairAssetId": "b6c4dd37-586a-486b-8ce3-846355a991a8",
        "Metadata": {
          "Weight": 70.0
        }
      },
      {
        "MapModePairAssetId": "8af8cd13-346d-4928-aa48-3bcb549ec806",
        "Metadata": {
          "Weight": 70.0
        }
      },
      {
        "MapModePairAssetId": "142e8555-5253-4e57-a2e2-b58adb9c1e28",
        "Metadata": {
          "Weight": 140.0
        }
      },
      {
        "MapModePairAssetId": "91957e4b-b5e4-4a11-ac69-dce934fa7002",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "8d598c79-07e5-4c11-9965-f2769822f9e0",
        "Metadata": {
          "Weight": 30.0
        }
      },
      {
        "MapModePairAssetId": "809acbc9-80c5-4f1b-b6e2-83c3e6a8adbc",
        "Metadata": {
          "Weight": 40.0
        }
      },
      {
        "MapModePairAssetId": "d62e9faa-b814-487a-8af9-972915b2b2ee",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "a228654f-9747-4afd-8950-5d3bc8572b2f",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "0bdce608-1877-4002-939f-ef205fbeb205",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "808a7472-a8fb-4ad5-90b9-ded5346b102e",
        "Metadata": {
          "Weight": 30.0
        }
      },
      {
        "MapModePairAssetId": "be1c791b-fbae-4e8d-aeee-9f48df6fee9d",
        "Metadata": {
          "Weight": 30.0
        }
      },
      {
        "MapModePairAssetId": "f1cbeead-e970-44c8-bb7c-966c431cd6c2",
        "Metadata": {
          "Weight": 30.0
        }
      },
      {
        "MapModePairAssetId": "f62707c5-fff3-4d8e-9ce4-68533c0ab003",
        "Metadata": {
          "Weight": 40.0
        }
      },
      {
        "MapModePairAssetId": "bfca483c-6abf-48b4-aae7-0c58e4c77fc9",
        "Metadata": {
          "Weight": 30.0
        }
      },
      {
        "MapModePairAssetId": "d19bdb97-0b7d-4573-a4d5-a32a4c526e1d",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "2f033099-4c32-414e-b9a3-d5b79084f1bd",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "8bdb2396-ae99-4e7c-a7ac-efe708c9b595",
        "Metadata": {
          "Weight": 65.0
        }
      },
      {
        "MapModePairAssetId": "6fdcc315-d996-4e8a-9a59-921b5d5e6437",
        "Metadata": {
          "Weight": 30.0
        }
      },
      {
        "MapModePairAssetId": "6963c343-8388-4610-a516-0bdff5fc7e49",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "be75354a-95e8-43f5-9bc0-f97886fce165",
        "Metadata": {
          "Weight": 175.0
        }
      },
      {
        "MapModePairAssetId": "92c406d7-04eb-4a86-832b-88bf9f3eb8ea",
        "Metadata": {
          "Weight": 100.0
        }
      },
      {
        "MapModePairAssetId": "199a7f3d-cf77-4f4b-b5ff-2273b56c472e",
        "Metadata": {
          "Weight": 150.0
        }
      },
      {
        "MapModePairAssetId": "d25ce1c0-7c40-4d79-b127-ec2cc6dd01dd",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "a0d112fa-4fa3-42e1-ba45-f042edafb346",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "9574a6fc-c0dc-4035-97b3-e645465e204a",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "30b2e8b1-07a8-495a-aae5-1f0e67a3b634",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "f9fa5035-cf60-4804-b3d9-59bd1566a8c8",
        "Metadata": {
          "Weight": 30.0
        }
      },
      {
        "MapModePairAssetId": "2a981fd7-7aff-4e37-ac07-ab20a95c42ec",
        "Metadata": {
          "Weight": 30.0
        }
      },
      {
        "MapModePairAssetId": "13e712d8-1f0d-4a3d-85ae-8e10474325a7",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "4a44deb2-580a-4f8f-9bb0-a45e45f7919d",
        "Metadata": {
          "Weight": 80.0
        }
      },
      {
        "MapModePairAssetId": "4d6d92f1-8cb3-4532-9e62-814cc7aee67c",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "7a772aa9-ba1a-4f92-82ae-afe0f4119e39",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "0195bc86-bc92-4365-9bf6-2d56f622e46a",
        "Metadata": {
          "Weight": 30.0
        }
      },
      {
        "MapModePairAssetId": "28748ed9-d73e-46d4-86dc-68c7deb4ad49",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "b0d7a2a5-1312-41f0-8842-9fd29ef83c2e",
        "Metadata": {
          "Weight": 20.0
        }
      },
      {
        "MapModePairAssetId": "9f76e66f-f6e8-4ba9-8340-91e2feee64b6",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "4aa35370-79dd-4e34-891d-710bcdfa226a",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "cd287634-1977-4acf-be58-3397d295bdd2",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "8707d3ca-1372-4351-966b-6b5318dfb70a",
        "Metadata": {
          "Weight": 20.0
        }
      },
      {
        "MapModePairAssetId": "b81af880-82b2-45a5-8ef8-f2a50c2728a5",
        "Metadata": {
          "Weight": 20.0
        }
      },
      {
        "MapModePairAssetId": "6de8098a-fdfd-45d6-b350-f242baa619a8",
        "Metadata": {
          "Weight": 50.0
        }
      },
      {
        "MapModePairAssetId": "bdab6069-d931-4291-a7d7-8481ffb51319",
        "Metadata": {
          "Weight": 40.0
        }
      },
      {
        "MapModePairAssetId": "5828e252-4283-41b2-a56e-0b3789f152ee",
        "Metadata": {
          "Weight": 60.0
        }
      },
      {
        "MapModePairAssetId": "5b72080b-b353-4097-a6b1-ed520d1679b3",
        "Metadata": {
          "Weight": 40.0
        }
      },
      {
        "MapModePairAssetId": "b0c8c5e1-e0a8-4de5-8b0a-c52896c93dfa",
        "Metadata": {
          "Weight": 40.0
        }
      }
    ],
    "Strategy": 0,
    "MinTeams": 2,
    "MinTeamSize": 4,
    "MaxTeams": 2,
    "MaxTeamSize": 4,
    "MaxTeamImbalance": 0,
    "MaxSplitscreenPlayersAllowed": 4,
    "AllowFriendJoinInProgress": false,
    "AllowMatchmakingJoinInProgress": false,
    "AllowBotJoinInProgress": false,
    "ExitExperienceDurationSec": 30,
    "FireteamLeaderKickAllowed": false,
    "DisableMidgameChat": false,
    "AllowedDeviceInputs": [
      0
    ],
    "BotDifficulty": 0,
    "MinFireteamSize": 1,
    "MaxFireteamSize": 4
  },
  "Tags": [],
  "RotationEntries": [
    {
      "Metadata": {
        "Weight": 30.0
      },
      "AssetId": "8d598c79-07e5-4c11-9965-f2769822f9e0",
      "VersionId": "1ade0b7b-b294-4919-8442-3624d693abca",
      "PublicName": "Ranked:King of the Hill on Recharge",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/8d598c79-07e5-4c11-9965-f2769822f9e0/1ade0b7b-b294-4919-8442-3624d693abca/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/8d598c79-07e5-4c11-9965-f2769822f9e0/1ade0b7b-b294-4919-8442-3624d693abca/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 1894,
        "PlaysAllTime": 2473753,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 40.0
      },
      "AssetId": "f62707c5-fff3-4d8e-9ce4-68533c0ab003",
      "VersionId": "80709eb4-075b-4708-85f2-00e143509bf4",
      "PublicName": "Ranked:Slayer on Solitude",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/f62707c5-fff3-4d8e-9ce4-68533c0ab003/80709eb4-075b-4708-85f2-00e143509bf4/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/f62707c5-fff3-4d8e-9ce4-68533c0ab003/80709eb4-075b-4708-85f2-00e143509bf4/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2524,
        "PlaysAllTime": 2061709,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 40.0
      },
      "AssetId": "b0c8c5e1-e0a8-4de5-8b0a-c52896c93dfa",
      "VersionId": "c766b722-d5de-47dc-92fb-d650f51aa9c5",
      "PublicName": "Ranked:Oddball on Streets - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/b0c8c5e1-e0a8-4de5-8b0a-c52896c93dfa/c766b722-d5de-47dc-92fb-d650f51aa9c5/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/b0c8c5e1-e0a8-4de5-8b0a-c52896c93dfa/c766b722-d5de-47dc-92fb-d650f51aa9c5/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2582,
        "PlaysAllTime": 68638,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 2,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 40.0
      },
      "AssetId": "bdab6069-d931-4291-a7d7-8481ffb51319",
      "VersionId": "7b1c58b7-df47-44b3-9bd2-e9f9285c9546",
      "PublicName": "Ranked:Slayer on Vacancy - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/bdab6069-d931-4291-a7d7-8481ffb51319/7b1c58b7-df47-44b3-9bd2-e9f9285c9546/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/bdab6069-d931-4291-a7d7-8481ffb51319/7b1c58b7-df47-44b3-9bd2-e9f9285c9546/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2522,
        "PlaysAllTime": 58107,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 2,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 30.0
      },
      "AssetId": "be1c791b-fbae-4e8d-aeee-9f48df6fee9d",
      "VersionId": "f2eb94d4-b02f-4da7-a4af-6aec7292ca63",
      "PublicName": "Ranked:Slayer on Live Fire",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/be1c791b-fbae-4e8d-aeee-9f48df6fee9d/f2eb94d4-b02f-4da7-a4af-6aec7292ca63/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/be1c791b-fbae-4e8d-aeee-9f48df6fee9d/f2eb94d4-b02f-4da7-a4af-6aec7292ca63/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 1944,
        "PlaysAllTime": 1863943,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 40.0
      },
      "AssetId": "809acbc9-80c5-4f1b-b6e2-83c3e6a8adbc",
      "VersionId": "d8da727f-7de6-4e10-94b4-25a1c98953a5",
      "PublicName": "Ranked:King of the Hill on Solitude",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/809acbc9-80c5-4f1b-b6e2-83c3e6a8adbc/d8da727f-7de6-4e10-94b4-25a1c98953a5/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/809acbc9-80c5-4f1b-b6e2-83c3e6a8adbc/d8da727f-7de6-4e10-94b4-25a1c98953a5/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2503,
        "PlaysAllTime": 2549185,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 60.0
      },
      "AssetId": "2f033099-4c32-414e-b9a3-d5b79084f1bd",
      "VersionId": "8499d8c8-cc84-4c62-a604-a4ec86291d05",
      "PublicName": "Ranked:Strongholds on Recharge",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/2f033099-4c32-414e-b9a3-d5b79084f1bd/8499d8c8-cc84-4c62-a604-a4ec86291d05/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/2f033099-4c32-414e-b9a3-d5b79084f1bd/8499d8c8-cc84-4c62-a604-a4ec86291d05/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3811,
        "PlaysAllTime": 2884534,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 50.0
      },
      "AssetId": "9f76e66f-f6e8-4ba9-8340-91e2feee64b6",
      "VersionId": "48bbdc40-3e43-4220-831f-1e0def86cab6",
      "PublicName": "Ranked:King of the Hill on Lattice - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/9f76e66f-f6e8-4ba9-8340-91e2feee64b6/48bbdc40-3e43-4220-831f-1e0def86cab6/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/9f76e66f-f6e8-4ba9-8340-91e2feee64b6/48bbdc40-3e43-4220-831f-1e0def86cab6/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3161,
        "PlaysAllTime": 138565,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 5,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 30.0
      },
      "AssetId": "f1cbeead-e970-44c8-bb7c-966c431cd6c2",
      "VersionId": "f54c62bf-623f-4d0c-8484-989a2d5a385b",
      "PublicName": "Ranked:Slayer on Recharge",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/f1cbeead-e970-44c8-bb7c-966c431cd6c2/f54c62bf-623f-4d0c-8484-989a2d5a385b/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/f1cbeead-e970-44c8-bb7c-966c431cd6c2/f54c62bf-623f-4d0c-8484-989a2d5a385b/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 1862,
        "PlaysAllTime": 1825286,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 50.0
      },
      "AssetId": "4aa35370-79dd-4e34-891d-710bcdfa226a",
      "VersionId": "453c720a-4ce5-4f8b-b03d-9fe2759f4148",
      "PublicName": "Ranked:Oddball on Lattice - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/4aa35370-79dd-4e34-891d-710bcdfa226a/453c720a-4ce5-4f8b-b03d-9fe2759f4148/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/4aa35370-79dd-4e34-891d-710bcdfa226a/453c720a-4ce5-4f8b-b03d-9fe2759f4148/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3157,
        "PlaysAllTime": 135732,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 5,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 60.0
      },
      "AssetId": "28748ed9-d73e-46d4-86dc-68c7deb4ad49",
      "VersionId": "9991e857-8427-4a86-91e6-e28c7f1d388d",
      "PublicName": "Ranked:CTF 3 Captures on Origin - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/28748ed9-d73e-46d4-86dc-68c7deb4ad49/9991e857-8427-4a86-91e6-e28c7f1d388d/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/28748ed9-d73e-46d4-86dc-68c7deb4ad49/9991e857-8427-4a86-91e6-e28c7f1d388d/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3686,
        "PlaysAllTime": 2168254,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 7,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 60.0
      },
      "AssetId": "5828e252-4283-41b2-a56e-0b3789f152ee",
      "VersionId": "6f1b51dc-434a-4a4a-bbd1-c5b50d3ead93",
      "PublicName": "Ranked:King of the Hill on Vacancy - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/5828e252-4283-41b2-a56e-0b3789f152ee/6f1b51dc-434a-4a4a-bbd1-c5b50d3ead93/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/5828e252-4283-41b2-a56e-0b3789f152ee/6f1b51dc-434a-4a4a-bbd1-c5b50d3ead93/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3808,
        "PlaysAllTime": 80877,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 2,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 60.0
      },
      "AssetId": "d19bdb97-0b7d-4573-a4d5-a32a4c526e1d",
      "VersionId": "53a76aac-819c-4bf5-9b4c-a6f9ec7fa242",
      "PublicName": "Ranked:Strongholds on Live Fire",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/d19bdb97-0b7d-4573-a4d5-a32a4c526e1d/53a76aac-819c-4bf5-9b4c-a6f9ec7fa242/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/d19bdb97-0b7d-4573-a4d5-a32a4c526e1d/53a76aac-819c-4bf5-9b4c-a6f9ec7fa242/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3877,
        "PlaysAllTime": 3186957,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 50.0
      },
      "AssetId": "91957e4b-b5e4-4a11-ac69-dce934fa7002",
      "VersionId": "f466779d-220d-4bf7-a817-a08e295537b9",
      "PublicName": "Ranked:King of the Hill on Live Fire",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/91957e4b-b5e4-4a11-ac69-dce934fa7002/f466779d-220d-4bf7-a817-a08e295537b9/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/91957e4b-b5e4-4a11-ac69-dce934fa7002/f466779d-220d-4bf7-a817-a08e295537b9/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3191,
        "PlaysAllTime": 2498566,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 30.0
      },
      "AssetId": "bfca483c-6abf-48b4-aae7-0c58e4c77fc9",
      "VersionId": "22a0ecc1-89ab-4efb-a0d5-39f0c04ea96d",
      "PublicName": "Ranked:Slayer on Streets",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/bfca483c-6abf-48b4-aae7-0c58e4c77fc9/22a0ecc1-89ab-4efb-a0d5-39f0c04ea96d/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/bfca483c-6abf-48b4-aae7-0c58e4c77fc9/22a0ecc1-89ab-4efb-a0d5-39f0c04ea96d/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 1997,
        "PlaysAllTime": 1914759,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 40.0
      },
      "AssetId": "5b72080b-b353-4097-a6b1-ed520d1679b3",
      "VersionId": "b536c2cb-4609-4adb-8062-0cd40b5b20eb",
      "PublicName": "Ranked:Oddball on Vacancy - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/5b72080b-b353-4097-a6b1-ed520d1679b3/b536c2cb-4609-4adb-8062-0cd40b5b20eb/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/5b72080b-b353-4097-a6b1-ed520d1679b3/b536c2cb-4609-4adb-8062-0cd40b5b20eb/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 2580,
        "PlaysAllTime": 68218,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 2,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 30.0
      },
      "AssetId": "f9fa5035-cf60-4804-b3d9-59bd1566a8c8",
      "VersionId": "5c4e77cf-9e9c-496c-b909-282b7d8dd0dd",
      "PublicName": "Ranked:CTF 3 Captures on Fortress - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/f9fa5035-cf60-4804-b3d9-59bd1566a8c8/5c4e77cf-9e9c-496c-b909-282b7d8dd0dd/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/f9fa5035-cf60-4804-b3d9-59bd1566a8c8/5c4e77cf-9e9c-496c-b909-282b7d8dd0dd/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 1935,
        "PlaysAllTime": 2227124,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 8,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 60.0
      },
      "AssetId": "a39b04bf-9c4a-42f0-8b30-81acdc3e1e83",
      "VersionId": "946401b1-4cef-460e-b39b-344b6d2db0c2",
      "PublicName": "Ranked:CTF 3 Captures on Empyrean",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/a39b04bf-9c4a-42f0-8b30-81acdc3e1e83/946401b1-4cef-460e-b39b-344b6d2db0c2/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/a39b04bf-9c4a-42f0-8b30-81acdc3e1e83/946401b1-4cef-460e-b39b-344b6d2db0c2/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3684,
        "PlaysAllTime": 1543851,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 70.0
      },
      "AssetId": "2bb084c2-a047-4fe9-9023-4100cbe6860d",
      "VersionId": "54b3f1da-a76a-4f71-9438-f775c0d7458a",
      "PublicName": "Ranked:CTF 5 Captures on Aquarius",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/2bb084c2-a047-4fe9-9023-4100cbe6860d/54b3f1da-a76a-4f71-9438-f775c0d7458a/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/2bb084c2-a047-4fe9-9023-4100cbe6860d/54b3f1da-a76a-4f71-9438-f775c0d7458a/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 4308,
        "PlaysAllTime": 2306666,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 30.0
      },
      "AssetId": "0195bc86-bc92-4365-9bf6-2d56f622e46a",
      "VersionId": "2fb65f40-568c-49da-a974-d81f9a705430",
      "PublicName": "Ranked:Slayer on Origin - Ranked",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/0195bc86-bc92-4365-9bf6-2d56f622e46a/2fb65f40-568c-49da-a974-d81f9a705430/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/0195bc86-bc92-4365-9bf6-2d56f622e46a/2fb65f40-568c-49da-a974-d81f9a705430/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 1856,
        "PlaysAllTime": 1525967,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 7,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.73aafd5a-29e8-4688-99d5-b2a44ed9c801)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 50.0
      },
      "AssetId": "d62e9faa-b814-487a-8af9-972915b2b2ee",
      "VersionId": "28fa2933-d66b-4b69-9874-247318881a07",
      "PublicName": "Ranked:Oddball on Live Fire",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/d62e9faa-b814-487a-8af9-972915b2b2ee/28fa2933-d66b-4b69-9874-247318881a07/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/d62e9faa-b814-487a-8af9-972915b2b2ee/28fa2933-d66b-4b69-9874-247318881a07/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3096,
        "PlaysAllTime": 2121100,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    },
    {
      "Metadata": {
        "Weight": 50.0
      },
      "AssetId": "a228654f-9747-4afd-8950-5d3bc8572b2f",
      "VersionId": "20ad7cc0-16d5-479d-8163-9034c4585356",
      "PublicName": "Ranked:Oddball on Recharge",
      "Description": "",
      "Files": {
        "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/mapmodepair/a228654f-9747-4afd-8950-5d3bc8572b2f/20ad7cc0-16d5-479d-8163-9034c4585356/",
        "FileRelativePaths": [],
        "PrefixEndpoint": {
          "AuthorityId": "iUgcFiles",
          "Path": "/ugcstorage/mapmodepair/a228654f-9747-4afd-8950-5d3bc8572b2f/20ad7cc0-16d5-479d-8163-9034c4585356/",
          "QueryString": null,
          "RetryPolicyId": "linearretry",
          "TopicName": "",
          "AcknowledgementTypeId": 0,
          "AuthenticationLifetimeExtensionSupported": false,
          "ClearanceAware": false
        }
      },
      "Contributors": [],
      "AssetHome": 1,
      "AssetStats": {
        "PlaysRecent": 3094,
        "PlaysAllTime": 2165086,
        "Favorites": 0,
        "Likes": 0,
        "Bookmarks": 0,
        "ParentAssetCount": 1,
        "AverageRating": 0.0,
        "NumberOfRatings": 0
      },
      "InspectionResult": 0,
      "CloneBehavior": 0,
      "Order": 0,
      "PublishedDate": null,
      "VersionNumber": 21,
      "Admin": "atui(27d5a614-5e32-4ce9-9207-b3a63945b5bb.b613328e-1f2a-4709-a9f1-d483d701a573)",
      "DisplayOwnerOverride": ""
    }
  ],
  "AssetId": "edfef3ac-9cbe-4fa2-b949-8f29deafd483",
  "VersionId": "37dd70c7-3ee7-4c87-b725-4b1a08d1b55d",
  "PublicName": "Ranked Arena",
  "Description": "[RANKED] [4v4] Bandit Evo loadout. Motion tracker disabled. Team Slayer, CTF, Oddball, KOTH, and Strongholds gametypes. Face off against other Spartans to earn or progress your rank.",
  "Files": {
    "Prefix": "https://blobs-infiniteugc.svc.halowaypoint.com/ugcstorage/playlist/edfef3ac-9cbe-4fa2-b949-8f29deafd483/37dd70c7-3ee7-4c87-b725-4b1a08d1b55d/",
    "FileRelativePaths": [
      "images/hero.jpg",
      "images/hero.png",
      "images/screenshot1.jpg",
      "images/screenshot1.png",
      "images/thumbnail.jpg",
      "images/thumbnail.png"
    ],
    "PrefixEndpoint": {
      "AuthorityId": "iUgcFiles",
      "Path": "/ugcstorage/playlist/edfef3ac-9cbe-4fa2-b949-8f29deafd483/37dd70c7-3ee7-4c87-b725-4b1a08d1b55d/",
      "QueryString": null,
      "RetryPolicyId": "linearretry",
      "TopicName": "",
      "AcknowledgementTypeId": 0,
      "AuthenticationLifetimeExtensionSupported": false,
      "ClearanceAware": false
    }
  },
  "Contributors": [],
  "AssetHome": 1,
  "AssetStats": {
    "PlaysRecent": 0,
    "PlaysAllTime": 0,
    "Favorites": 1,
    "Likes": 0,
    "Bookmarks": 0,
    "ParentAssetCount": 13,
    "AverageRating": 0.0,
    "NumberOfRatings": 0
  },
  "InspectionResult": 0,
  "CloneBehavior": 0,
  "Order": 0,
  "PublishedDate": null,
  "VersionNumber": 57,
  "Admin": "auid(8eb20a3e-04db-45c1-85b8-db7adbbf1836)",
  "DisplayOwnerOverride": ""
}
  ```


## Table: `ServiceRecordSnapshots`

### Schema
```sql
CREATE TABLE ServiceRecordSnapshots (

	ResponseBody TEXT,

	SnapshotTimestamp DATETIME,

	Subqueries Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Subqueries')) VIRTUAL,

	TimePlayed Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.TimePlayed')) VIRTUAL,

	MatchesCompleted Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.MatchesCompleted')) VIRTUAL,

	Wins Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Wins')) VIRTUAL,

	Losses Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Losses')) VIRTUAL,

	Ties Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.Ties')) VIRTUAL,

	CoreStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CoreStats')) VIRTUAL,

	BombStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.BombStats')) VIRTUAL,

	CaptureTheFlagStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.CaptureTheFlagStats')) VIRTUAL,

	EliminationStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.EliminationStats')) VIRTUAL,

	ExtractionStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.ExtractionStats')) VIRTUAL,

	InfectionStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.InfectionStats')) VIRTUAL,

	OddballStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.OddballStats')) VIRTUAL,

	ZonesStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.ZonesStats')) VIRTUAL,

	StockpileStats Text GENERATED ALWAYS AS (json_extract(ResponseBody, '$.StockpileStats')) VIRTUAL

)
```

**Records: 4**

### Sample Row 1

- **ResponseBody**:
  ```json
  {
  "Subqueries": {
    "SeasonIds": [
      "Seasons/Season6.json",
      "Seasons/Season6-2.json",
      "Seasons/Season7.json",
      "Seasons/Season-Winter-Break-22.json",
      "Seasons/Season3.json",
      "Csr/Seasons/CsrSeason5-1.json",
      "Csr/Seasons/CsrSeason13-2.json"
    ],
    "GameVariantCategories": [
      6,
      15,
      11,
      18,
      19,
      14,
      9,
      12,
      7,
      39,
      24,
      17
    ],
    "IsRanked": [
      false,
      true
    ],
    "PlaylistAssetIds": [
      "bdceefb3-1c52-4848-a6b7-d49acd13109d",
      "edfef3ac-9cbe-4fa2-b949-8f29deafd483",
      "dc4929de-216c-43bc-b207-1702253f4576",
      "f7f30787-f607-436b-bdec-44c65bc2ecef",
      "a446725e-b281-414c-a21e-31b8700e95a1",
      "4af0b113-8696-4f22-9e09-596d473de933",
      "7f2b4f8f-c2f3-4ad4-a250-b55214fa4111",
      "325c18a5-d85b-4ba6-b98f-21465d9c19e2",
      "aa41f6a9-51be-4f25-a53f-48192ce14de7",
      "7d9828c7-8184-4421-ad14-824fce8f7ebe",
      "0299adc1-f07a-4b6c-8126-0c35ac2fa08d",
      "70bb9184-e674-4307-8846-239ab4a30cb6",
      "14352c39-a409-4d34-9ded-1c280bb4f868",
      "3facc347-6e49-40c9-b9e7-503d26092eed",
      "fa5aa2a3-2428-4912-a023-e1eeea7b877c",
      "73b48e1e-05c4-4004-927d-965549b28396",
      "7de5ed5b-381e-49e5-b334-d959056dbc2b",
      "71734db4-4b8e-4682-9206-62b6eff92582",
      "4da919eb-5368-4954-90f5-7e88d678ace7",
      "af3cef4b-4837-4d75-b680-0ffe6190009b",
      "4829f027-a9af-4b2f-86dd-7b290d6bb0a4",
      "4795cb47-5b32-4c87-98ab-02f12e94ca31",
      "90eb5903-0a0d-46b8-973a-8f4fc93edbce",
      "d22aa90d-3091-4214-a85e-c968037cef2f",
      "6233381c-fc96-40b9-b1ff-f6a4de72dd7a",
      "dcb2e24e-05fb-4390-8076-32a0cdb4326e",
      "1b1691dc-d8b9-4b1f-825d-cb1c065184c1",
      "7323be09-2523-47c0-9e0d-64af9534ee22"
    ],
    "GameplayInteractions": null
  },
  "TimePlayed": "P17DT15H17M47.2981498S",
  "MatchesCompleted": 2482,
  "Wins": 1320,
  "Losses": 1106,
  "Ties": 50,
  "CoreStats": {
    "Score": 28580,
    "PersonalScore": 4781560,
    "RoundsWon": 1561,
    "RoundsLost": 1358,
    "RoundsTied": 156,
    "Kills": 34308,
    "Deaths": 33048,
    "Assists": 15538,
    "AverageKDA": 2.594413107708838,
    "Suicides": 39,
    "Betrayals": 12,
    "GrenadeKills": 1887,
    "HeadshotKills": 22972,
    "MeleeKills": 3645,
    "PowerWeaponKills": 3025,
    "ShotsFired": 974519,
    "ShotsHit": 501370,
    "Accuracy": 51.44794508880791,
    "DamageDealt": 10362835,
    "DamageTaken": 10594300,
    "CalloutAssists": 677,
    "VehicleDestroys": 63,
    "DriverAssists": 6,
    "Hijacks": 13,
    "EmpAssists": 3,
    "MaxKillingSpree": 16,
    "Medals": [
      {
        "NameId": 2602963073,
        "Count": 400,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 622331684,
        "Count": 2594,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2852571933,
        "Count": 221,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2780740615,
        "Count": 819,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2063152177,
        "Count": 204,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2758320809,
        "Count": 1767,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1512363953,
        "Count": 1570,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1169390319,
        "Count": 56,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4215552487,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2861418269,
        "Count": 36,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 548533137,
        "Count": 794,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1176569867,
        "Count": 86,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3233952928,
        "Count": 675,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1283796619,
        "Count": 85,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2123530881,
        "Count": 563,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2418616582,
        "Count": 36,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1284032216,
        "Count": 437,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3546244406,
        "Count": 21,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2625820422,
        "Count": 360,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2477555653,
        "Count": 4,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3091261182,
        "Count": 88,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4229934157,
        "Count": 614,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 265478668,
        "Count": 25,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1169571763,
        "Count": 269,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4277328263,
        "Count": 103,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3334154676,
        "Count": 182,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 269174970,
        "Count": 124,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4132863117,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3732790338,
        "Count": 36,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3655682764,
        "Count": 205,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1427176344,
        "Count": 8,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3227840152,
        "Count": 31,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2414983178,
        "Count": 22,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3488248720,
        "Count": 34,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3160646854,
        "Count": 8,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1472686630,
        "Count": 12,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 670606868,
        "Count": 6,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3630529364,
        "Count": 9,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3347922939,
        "Count": 17,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 555849395,
        "Count": 13,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 524758914,
        "Count": 16,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3217141618,
        "Count": 10,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1172766553,
        "Count": 39,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 87172902,
        "Count": 6,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1734214473,
        "Count": 56,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1969067783,
        "Count": 10,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3934547153,
        "Count": 32,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3905838030,
        "Count": 20,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2648272972,
        "Count": 11,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3114137341,
        "Count": 15,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4261842076,
        "Count": 22,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 418532952,
        "Count": 6,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 865763896,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 835814121,
        "Count": 16,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1211820913,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 221693153,
        "Count": 10,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 690125105,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1646928910,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1146876011,
        "Count": 13,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 731054446,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1880789493,
        "Count": 49,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1210678802,
        "Count": 11,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 781229683,
        "Count": 13,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3085856613,
        "Count": 9,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 580478179,
        "Count": 51,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1477806194,
        "Count": 163,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3876426273,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1486797009,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 710323196,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 651256911,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 656245292,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3528500956,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 275666139,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1623236079,
        "Count": 3,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 641726424,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1229018603,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2278023431,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2593226288,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 988255960,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2827657131,
        "Count": 3,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3059799290,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2396845048,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1680000231,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1312042926,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1841872491,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 394349536,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2964157454,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      }
    ],
    "PersonalScores": [
      {
        "NameId": 1024030246,
        "Count": 34287,
        "TotalPersonalScoreAwarded": 1700
      },
      {
        "NameId": 638246808,
        "Count": 15475,
        "TotalPersonalScoreAwarded": 150
      },
      {
        "NameId": 597066859,
        "Count": 5,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 22113181,
        "Count": 412,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 316828380,
        "Count": 305,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 3507884073,
        "Count": 2264,
        "TotalPersonalScoreAwarded": 500
      },
      {
        "NameId": 709346128,
        "Count": 810,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 746397417,
        "Count": 576,
        "TotalPersonalScoreAwarded": 75
      },
      {
        "NameId": 204144695,
        "Count": 1724,
        "TotalPersonalScoreAwarded": 40
      },
      {
        "NameId": 454168309,
        "Count": 2733,
        "TotalPersonalScoreAwarded": 350
      },
      {
        "NameId": 1834653062,
        "Count": 2,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 963594075,
        "Count": 6,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 152718958,
        "Count": 677,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 3996338664,
        "Count": 2,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 4128329646,
        "Count": 6,
        "TotalPersonalScoreAwarded": 10
      },
      {
        "NameId": 3002710045,
        "Count": 822,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 2387185397,
        "Count": 581,
        "TotalPersonalScoreAwarded": 60
      },
      {
        "NameId": 601966503,
        "Count": 251,
        "TotalPersonalScoreAwarded": 300
      },
      {
        "NameId": 555570945,
        "Count": 228,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 3472794399,
        "Count": 3,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 249491819,
        "Count": 39,
        "TotalPersonalScoreAwarded": -100
      },
      {
        "NameId": 3107879375,
        "Count": 10,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 911992497,
        "Count": 12,
        "TotalPersonalScoreAwarded": -100
      },
      {
        "NameId": 4254982885,
        "Count": 11,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 1614285349,
        "Count": 8,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 1059880024,
        "Count": 1,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 3150095814,
        "Count": 2,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 340198991,
        "Count": 2903,
        "TotalPersonalScoreAwarded": 275
      },
      {
        "NameId": 1032565232,
        "Count": 269,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 2188620691,
        "Count": 18,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 2801241965,
        "Count": 8,
        "TotalPersonalScoreAwarded": 150
      },
      {
        "NameId": 522435689,
        "Count": 17,
        "TotalPersonalScoreAwarded": 1000
      },
      {
        "NameId": 2408971842,
        "Count": 20,
        "TotalPersonalScoreAwarded": 200
      },
      {
        "NameId": 665081740,
        "Count": 12,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 757037588,
        "Count": 102,
        "TotalPersonalScoreAwarded": 600
      },
      {
        "NameId": 4026987576,
        "Count": 39,
        "TotalPersonalScoreAwarded": 375
      },
      {
        "NameId": 2106274556,
        "Count": 2,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 221060588,
        "Count": 3,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 2107631925,
        "Count": 1,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 3243589708,
        "Count": 3,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 2008690931,
        "Count": 1,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 1267013266,
        "Count": 13,
        "TotalPersonalScoreAwarded": 20
      },
      {
        "NameId": 3454330054,
        "Count": 1,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 4130011565,
        "Count": 4,
        "TotalPersonalScoreAwarded": 200
      },
      {
        "NameId": 1117301492,
        "Count": 1,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 4247243561,
        "Count": 1,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 1825517751,
        "Count": 1,
        "TotalPersonalScoreAwarded": 50
      }
    ],
    "Spawns": 26740,
    "ObjectivesCompleted": 0
  },
  "CaptureTheFlagStats": {
    "FlagCaptureAssists": 228,
    "FlagCaptures": 251,
    "FlagCarriersKilled": 305,
    "FlagGrabs": 2881,
    "FlagReturnersKilled": 201,
    "FlagReturns": 412,
    "FlagSecures": 1972,
    "FlagSteals": 822,
    "KillsAsFlagCarrier": 17,
    "KillsAsFlagReturner": 73,
    "TimeAsFlagCarrier": "PT2H24M16.4S"
  },
  "EliminationStats": {
    "AlliesRevived": 0,
    "EliminationAssists": 6,
    "Eliminations": 20,
    "EnemyRevivesDenied": 0,
    "Executions": 17,
    "KillsAsLastPlayerStanding": 0,
    "LastPlayersStandingKilled": 1,
    "RoundsSurvived": 1,
    "TimesRevivedByAlly": 0
  },
  "ExtractionStats": {
    "SuccessfulExtractions": 1,
    "ExtractionConversionsDenied": 1,
    "ExtractionConversionsCompleted": 1,
    "ExtractionInitiationsDenied": 0,
    "ExtractionInitiationsCompleted": 1
  },
  "OddballStats": {
    "KillsAsSkullCarrier": 29,
    "LongestTimeAsSkullCarrier": "PT1M39.9S",
    "SkullCarriersKilled": 576,
    "SkullGrabs": 284,
    "TimeAsSkullCarrier": "PT5H12M18.9S",
    "SkullScoringTicks": 17596
  },
  "ZonesStats": {
    "ZoneCaptures": 4028,
    "ZoneDefensiveKills": 1491,
    "ZoneOffensiveKills": 2025,
    "ZoneSecures": 1062,
    "TotalZoneOccupationTime": "PT13H36M16.5S",
    "ZoneScoringTicks": 14476
  },
  "StockpileStats": {
    "KillsAsPowerSeedCarrier": 0,
    "PowerSeedCarriersKilled": 6,
    "PowerSeedsDeposited": 18,
    "PowerSeedsStolen": 2,
    "TimeAsPowerSeedCarrier": "PT6M45.8S",
    "TimeAsPowerSeedDriver": "PT0S"
  },
  "PvpStats": {
    "Kills": 2469,
    "Deaths": 2517,
    "Assists": 1209
  }
}
  ```
- **SnapshotTimestamp**: `2026-05-11T22:10:25.626+09:00`

### Sample Row 2

- **ResponseBody**:
  ```json
  {
  "Subqueries": {
    "SeasonIds": [
      "Seasons/Season6.json",
      "Seasons/Season6-2.json",
      "Seasons/Season7.json",
      "Seasons/Season-Winter-Break-22.json",
      "Seasons/Season3.json",
      "Csr/Seasons/CsrSeason5-1.json",
      "Csr/Seasons/CsrSeason13-2.json"
    ],
    "GameVariantCategories": [
      6,
      15,
      11,
      18,
      19,
      14,
      9,
      12,
      7,
      39,
      24,
      17
    ],
    "IsRanked": [
      false,
      true
    ],
    "PlaylistAssetIds": [
      "bdceefb3-1c52-4848-a6b7-d49acd13109d",
      "edfef3ac-9cbe-4fa2-b949-8f29deafd483",
      "dc4929de-216c-43bc-b207-1702253f4576",
      "f7f30787-f607-436b-bdec-44c65bc2ecef",
      "a446725e-b281-414c-a21e-31b8700e95a1",
      "4af0b113-8696-4f22-9e09-596d473de933",
      "7f2b4f8f-c2f3-4ad4-a250-b55214fa4111",
      "325c18a5-d85b-4ba6-b98f-21465d9c19e2",
      "aa41f6a9-51be-4f25-a53f-48192ce14de7",
      "7d9828c7-8184-4421-ad14-824fce8f7ebe",
      "0299adc1-f07a-4b6c-8126-0c35ac2fa08d",
      "70bb9184-e674-4307-8846-239ab4a30cb6",
      "14352c39-a409-4d34-9ded-1c280bb4f868",
      "3facc347-6e49-40c9-b9e7-503d26092eed",
      "fa5aa2a3-2428-4912-a023-e1eeea7b877c",
      "73b48e1e-05c4-4004-927d-965549b28396",
      "7de5ed5b-381e-49e5-b334-d959056dbc2b",
      "71734db4-4b8e-4682-9206-62b6eff92582",
      "4da919eb-5368-4954-90f5-7e88d678ace7",
      "af3cef4b-4837-4d75-b680-0ffe6190009b",
      "4829f027-a9af-4b2f-86dd-7b290d6bb0a4",
      "4795cb47-5b32-4c87-98ab-02f12e94ca31",
      "90eb5903-0a0d-46b8-973a-8f4fc93edbce",
      "d22aa90d-3091-4214-a85e-c968037cef2f",
      "6233381c-fc96-40b9-b1ff-f6a4de72dd7a",
      "dcb2e24e-05fb-4390-8076-32a0cdb4326e",
      "1b1691dc-d8b9-4b1f-825d-cb1c065184c1",
      "7323be09-2523-47c0-9e0d-64af9534ee22"
    ],
    "GameplayInteractions": null
  },
  "TimePlayed": "P17DT16H29M1.9861498S",
  "MatchesCompleted": 2492,
  "Wins": 1325,
  "Losses": 1110,
  "Ties": 51,
  "CoreStats": {
    "Score": 28673,
    "PersonalScore": 4791810,
    "RoundsWon": 1567,
    "RoundsLost": 1362,
    "RoundsTied": 157,
    "Kills": 34386,
    "Deaths": 33143,
    "Assists": 15578,
    "AverageKDA": 2.5825307651150338,
    "Suicides": 39,
    "Betrayals": 12,
    "GrenadeKills": 1889,
    "HeadshotKills": 23033,
    "MeleeKills": 3651,
    "PowerWeaponKills": 3025,
    "ShotsFired": 975779,
    "ShotsHit": 502045,
    "Accuracy": 51.450687092056704,
    "DamageDealt": 10390736,
    "DamageTaken": 10626489,
    "CalloutAssists": 689,
    "VehicleDestroys": 63,
    "DriverAssists": 6,
    "Hijacks": 13,
    "EmpAssists": 3,
    "MaxKillingSpree": 16,
    "Medals": [
      {
        "NameId": 2602963073,
        "Count": 400,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 622331684,
        "Count": 2596,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2852571933,
        "Count": 229,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2780740615,
        "Count": 819,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2063152177,
        "Count": 204,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2758320809,
        "Count": 1767,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1512363953,
        "Count": 1578,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1169390319,
        "Count": 56,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4215552487,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2861418269,
        "Count": 36,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 548533137,
        "Count": 794,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1176569867,
        "Count": 86,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3233952928,
        "Count": 677,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1283796619,
        "Count": 85,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2123530881,
        "Count": 564,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2418616582,
        "Count": 36,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1284032216,
        "Count": 438,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3546244406,
        "Count": 21,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2625820422,
        "Count": 361,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2477555653,
        "Count": 4,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3091261182,
        "Count": 88,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4229934157,
        "Count": 614,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 265478668,
        "Count": 25,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1169571763,
        "Count": 276,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4277328263,
        "Count": 103,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3334154676,
        "Count": 184,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 269174970,
        "Count": 124,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4132863117,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3732790338,
        "Count": 36,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3655682764,
        "Count": 205,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1427176344,
        "Count": 8,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3227840152,
        "Count": 31,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2414983178,
        "Count": 22,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3488248720,
        "Count": 34,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3160646854,
        "Count": 8,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1472686630,
        "Count": 12,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 670606868,
        "Count": 6,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3630529364,
        "Count": 9,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3347922939,
        "Count": 17,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 555849395,
        "Count": 13,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 524758914,
        "Count": 16,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3217141618,
        "Count": 10,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1172766553,
        "Count": 39,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 87172902,
        "Count": 6,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1734214473,
        "Count": 56,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1969067783,
        "Count": 10,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3934547153,
        "Count": 32,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3905838030,
        "Count": 20,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2648272972,
        "Count": 11,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3114137341,
        "Count": 15,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4261842076,
        "Count": 22,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 418532952,
        "Count": 6,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 865763896,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 835814121,
        "Count": 16,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1211820913,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 221693153,
        "Count": 10,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 690125105,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1646928910,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1146876011,
        "Count": 13,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 731054446,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1880789493,
        "Count": 49,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1210678802,
        "Count": 11,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 781229683,
        "Count": 13,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3085856613,
        "Count": 9,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 580478179,
        "Count": 51,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1477806194,
        "Count": 163,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3876426273,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1486797009,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 710323196,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 651256911,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 656245292,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3528500956,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 275666139,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1623236079,
        "Count": 3,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 641726424,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1229018603,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2278023431,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2593226288,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 988255960,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2827657131,
        "Count": 3,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3059799290,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2396845048,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1680000231,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1312042926,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1841872491,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 394349536,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2964157454,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      }
    ],
    "PersonalScores": [
      {
        "NameId": 1024030246,
        "Count": 34365,
        "TotalPersonalScoreAwarded": 1700
      },
      {
        "NameId": 638246808,
        "Count": 15515,
        "TotalPersonalScoreAwarded": 150
      },
      {
        "NameId": 597066859,
        "Count": 5,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 22113181,
        "Count": 412,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 316828380,
        "Count": 305,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 3507884073,
        "Count": 2264,
        "TotalPersonalScoreAwarded": 500
      },
      {
        "NameId": 709346128,
        "Count": 810,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 746397417,
        "Count": 576,
        "TotalPersonalScoreAwarded": 75
      },
      {
        "NameId": 204144695,
        "Count": 1727,
        "TotalPersonalScoreAwarded": 40
      },
      {
        "NameId": 454168309,
        "Count": 2738,
        "TotalPersonalScoreAwarded": 350
      },
      {
        "NameId": 1834653062,
        "Count": 2,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 963594075,
        "Count": 6,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 152718958,
        "Count": 689,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 3996338664,
        "Count": 2,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 4128329646,
        "Count": 6,
        "TotalPersonalScoreAwarded": 10
      },
      {
        "NameId": 3002710045,
        "Count": 824,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 2387185397,
        "Count": 581,
        "TotalPersonalScoreAwarded": 60
      },
      {
        "NameId": 601966503,
        "Count": 251,
        "TotalPersonalScoreAwarded": 300
      },
      {
        "NameId": 555570945,
        "Count": 228,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 3472794399,
        "Count": 3,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 249491819,
        "Count": 39,
        "TotalPersonalScoreAwarded": -100
      },
      {
        "NameId": 3107879375,
        "Count": 10,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 911992497,
        "Count": 12,
        "TotalPersonalScoreAwarded": -100
      },
      {
        "NameId": 4254982885,
        "Count": 11,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 1614285349,
        "Count": 8,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 1059880024,
        "Count": 1,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 3150095814,
        "Count": 2,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 340198991,
        "Count": 2903,
        "TotalPersonalScoreAwarded": 275
      },
      {
        "NameId": 1032565232,
        "Count": 269,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 2188620691,
        "Count": 18,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 2801241965,
        "Count": 8,
        "TotalPersonalScoreAwarded": 150
      },
      {
        "NameId": 522435689,
        "Count": 17,
        "TotalPersonalScoreAwarded": 1000
      },
      {
        "NameId": 2408971842,
        "Count": 20,
        "TotalPersonalScoreAwarded": 200
      },
      {
        "NameId": 665081740,
        "Count": 12,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 757037588,
        "Count": 102,
        "TotalPersonalScoreAwarded": 600
      },
      {
        "NameId": 4026987576,
        "Count": 39,
        "TotalPersonalScoreAwarded": 375
      },
      {
        "NameId": 2106274556,
        "Count": 2,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 221060588,
        "Count": 3,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 2107631925,
        "Count": 1,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 3243589708,
        "Count": 3,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 2008690931,
        "Count": 1,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 1267013266,
        "Count": 13,
        "TotalPersonalScoreAwarded": 20
      },
      {
        "NameId": 3454330054,
        "Count": 1,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 4130011565,
        "Count": 4,
        "TotalPersonalScoreAwarded": 200
      },
      {
        "NameId": 1117301492,
        "Count": 1,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 4247243561,
        "Count": 1,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 1825517751,
        "Count": 1,
        "TotalPersonalScoreAwarded": 50
      }
    ],
    "Spawns": 26844,
    "ObjectivesCompleted": 0
  },
  "CaptureTheFlagStats": {
    "FlagCaptureAssists": 228,
    "FlagCaptures": 251,
    "FlagCarriersKilled": 305,
    "FlagGrabs": 2881,
    "FlagReturnersKilled": 201,
    "FlagReturns": 412,
    "FlagSecures": 1972,
    "FlagSteals": 824,
    "KillsAsFlagCarrier": 17,
    "KillsAsFlagReturner": 73,
    "TimeAsFlagCarrier": "PT2H24M20.1S"
  },
  "EliminationStats": {
    "AlliesRevived": 0,
    "EliminationAssists": 6,
    "Eliminations": 20,
    "EnemyRevivesDenied": 0,
    "Executions": 17,
    "KillsAsLastPlayerStanding": 0,
    "LastPlayersStandingKilled": 1,
    "RoundsSurvived": 1,
    "TimesRevivedByAlly": 0
  },
  "ExtractionStats": {
    "SuccessfulExtractions": 1,
    "ExtractionConversionsDenied": 1,
    "ExtractionConversionsCompleted": 1,
    "ExtractionInitiationsDenied": 0,
    "ExtractionInitiationsCompleted": 1
  },
  "OddballStats": {
    "KillsAsSkullCarrier": 29,
    "LongestTimeAsSkullCarrier": "PT1M39.9S",
    "SkullCarriersKilled": 576,
    "SkullGrabs": 284,
    "TimeAsSkullCarrier": "PT5H12M55.6S",
    "SkullScoringTicks": 17631
  },
  "ZonesStats": {
    "ZoneCaptures": 4028,
    "ZoneDefensiveKills": 1491,
    "ZoneOffensiveKills": 2025,
    "ZoneSecures": 1062,
    "TotalZoneOccupationTime": "PT13H36M16.5S",
    "ZoneScoringTicks": 14476
  },
  "StockpileStats": {
    "KillsAsPowerSeedCarrier": 0,
    "PowerSeedCarriersKilled": 6,
    "PowerSeedsDeposited": 18,
    "PowerSeedsStolen": 2,
    "TimeAsPowerSeedCarrier": "PT6M45.8S",
    "TimeAsPowerSeedDriver": "PT0S"
  },
  "PvpStats": {
    "Kills": 2547,
    "Deaths": 2612,
    "Assists": 1249
  }
}
  ```
- **SnapshotTimestamp**: `2026-05-12T15:00:16.316+09:00`


---
## ServiceRecordSnapshots - Full Data (Most Recent)

```json
{
  "Subqueries": {
    "SeasonIds": [
      "Seasons/Season6.json",
      "Seasons/Season6-2.json",
      "Seasons/Season7.json",
      "Seasons/Season-Winter-Break-22.json",
      "Seasons/Season3.json",
      "Csr/Seasons/CsrSeason5-1.json",
      "Csr/Seasons/CsrSeason13-2.json"
    ],
    "GameVariantCategories": [
      6,
      15,
      11,
      18,
      19,
      14,
      9,
      12,
      7,
      39,
      24,
      17
    ],
    "IsRanked": [
      false,
      true
    ],
    "PlaylistAssetIds": [
      "bdceefb3-1c52-4848-a6b7-d49acd13109d",
      "edfef3ac-9cbe-4fa2-b949-8f29deafd483",
      "dc4929de-216c-43bc-b207-1702253f4576",
      "f7f30787-f607-436b-bdec-44c65bc2ecef",
      "a446725e-b281-414c-a21e-31b8700e95a1",
      "4af0b113-8696-4f22-9e09-596d473de933",
      "7f2b4f8f-c2f3-4ad4-a250-b55214fa4111",
      "325c18a5-d85b-4ba6-b98f-21465d9c19e2",
      "aa41f6a9-51be-4f25-a53f-48192ce14de7",
      "7d9828c7-8184-4421-ad14-824fce8f7ebe",
      "0299adc1-f07a-4b6c-8126-0c35ac2fa08d",
      "70bb9184-e674-4307-8846-239ab4a30cb6",
      "14352c39-a409-4d34-9ded-1c280bb4f868",
      "3facc347-6e49-40c9-b9e7-503d26092eed",
      "fa5aa2a3-2428-4912-a023-e1eeea7b877c",
      "73b48e1e-05c4-4004-927d-965549b28396",
      "7de5ed5b-381e-49e5-b334-d959056dbc2b",
      "71734db4-4b8e-4682-9206-62b6eff92582",
      "4da919eb-5368-4954-90f5-7e88d678ace7",
      "af3cef4b-4837-4d75-b680-0ffe6190009b",
      "4829f027-a9af-4b2f-86dd-7b290d6bb0a4",
      "4795cb47-5b32-4c87-98ab-02f12e94ca31",
      "90eb5903-0a0d-46b8-973a-8f4fc93edbce",
      "d22aa90d-3091-4214-a85e-c968037cef2f",
      "6233381c-fc96-40b9-b1ff-f6a4de72dd7a",
      "dcb2e24e-05fb-4390-8076-32a0cdb4326e",
      "1b1691dc-d8b9-4b1f-825d-cb1c065184c1",
      "7323be09-2523-47c0-9e0d-64af9534ee22"
    ],
    "GameplayInteractions": null
  },
  "TimePlayed": "P17DT18H55.0661498S",
  "MatchesCompleted": 2502,
  "Wins": 1328,
  "Losses": 1116,
  "Ties": 52,
  "CoreStats": {
    "Score": 28803,
    "PersonalScore": 4806745,
    "RoundsWon": 1571,
    "RoundsLost": 1370,
    "RoundsTied": 158,
    "Kills": 34498,
    "Deaths": 33262,
    "Assists": 15624,
    "AverageKDA": 2.5755395683453237,
    "Suicides": 39,
    "Betrayals": 12,
    "GrenadeKills": 1891,
    "HeadshotKills": 23115,
    "MeleeKills": 3665,
    "PowerWeaponKills": 3029,
    "ShotsFired": 977346,
    "ShotsHit": 502891,
    "Accuracy": 51.45475604340734,
    "DamageDealt": 10427367,
    "DamageTaken": 10667554,
    "CalloutAssists": 696,
    "VehicleDestroys": 63,
    "DriverAssists": 6,
    "Hijacks": 13,
    "EmpAssists": 3,
    "MaxKillingSpree": 16,
    "Medals": [
      {
        "NameId": 2602963073,
        "Count": 402,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 622331684,
        "Count": 2600,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2852571933,
        "Count": 237,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2780740615,
        "Count": 820,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2063152177,
        "Count": 204,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2758320809,
        "Count": 1767,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1512363953,
        "Count": 1586,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1169390319,
        "Count": 56,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4215552487,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2861418269,
        "Count": 36,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 548533137,
        "Count": 797,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1176569867,
        "Count": 86,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3233952928,
        "Count": 678,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1283796619,
        "Count": 85,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2123530881,
        "Count": 565,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2418616582,
        "Count": 36,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1284032216,
        "Count": 439,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3546244406,
        "Count": 21,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2625820422,
        "Count": 363,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2477555653,
        "Count": 4,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3091261182,
        "Count": 88,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4229934157,
        "Count": 615,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 265478668,
        "Count": 25,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1169571763,
        "Count": 279,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4277328263,
        "Count": 104,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3334154676,
        "Count": 184,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 269174970,
        "Count": 125,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4132863117,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3732790338,
        "Count": 36,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3655682764,
        "Count": 205,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1427176344,
        "Count": 8,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3227840152,
        "Count": 31,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2414983178,
        "Count": 22,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3488248720,
        "Count": 34,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3160646854,
        "Count": 8,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1472686630,
        "Count": 12,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 670606868,
        "Count": 6,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3630529364,
        "Count": 9,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3347922939,
        "Count": 17,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 555849395,
        "Count": 14,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 524758914,
        "Count": 16,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3217141618,
        "Count": 10,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1172766553,
        "Count": 39,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 87172902,
        "Count": 6,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1734214473,
        "Count": 56,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1969067783,
        "Count": 10,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3934547153,
        "Count": 32,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3905838030,
        "Count": 20,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2648272972,
        "Count": 11,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3114137341,
        "Count": 15,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 4261842076,
        "Count": 22,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 418532952,
        "Count": 6,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 865763896,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 835814121,
        "Count": 16,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1211820913,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 221693153,
        "Count": 10,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 690125105,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1646928910,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1146876011,
        "Count": 13,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 731054446,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1880789493,
        "Count": 49,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1210678802,
        "Count": 11,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 781229683,
        "Count": 13,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3085856613,
        "Count": 9,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 580478179,
        "Count": 51,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1477806194,
        "Count": 163,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3876426273,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1486797009,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 710323196,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 651256911,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 656245292,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3528500956,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 275666139,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1623236079,
        "Count": 3,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 641726424,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1229018603,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2278023431,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2593226288,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 988255960,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2827657131,
        "Count": 3,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 3059799290,
        "Count": 5,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2396845048,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1680000231,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1312042926,
        "Count": 2,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 1841872491,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 394349536,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      },
      {
        "NameId": 2964157454,
        "Count": 1,
        "TotalPersonalScoreAwarded": 0
      }
    ],
    "PersonalScores": [
      {
        "NameId": 1024030246,
        "Count": 34477,
        "TotalPersonalScoreAwarded": 1700
      },
      {
        "NameId": 638246808,
        "Count": 15561,
        "TotalPersonalScoreAwarded": 150
      },
      {
        "NameId": 597066859,
        "Count": 5,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 22113181,
        "Count": 412,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 316828380,
        "Count": 305,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 3507884073,
        "Count": 2275,
        "TotalPersonalScoreAwarded": 500
      },
      {
        "NameId": 709346128,
        "Count": 813,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 746397417,
        "Count": 578,
        "TotalPersonalScoreAwarded": 75
      },
      {
        "NameId": 204144695,
        "Count": 1731,
        "TotalPersonalScoreAwarded": 40
      },
      {
        "NameId": 454168309,
        "Count": 2750,
        "TotalPersonalScoreAwarded": 350
      },
      {
        "NameId": 1834653062,
        "Count": 2,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 963594075,
        "Count": 6,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 152718958,
        "Count": 696,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 3996338664,
        "Count": 2,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 4128329646,
        "Count": 6,
        "TotalPersonalScoreAwarded": 10
      },
      {
        "NameId": 3002710045,
        "Count": 824,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 2387185397,
        "Count": 581,
        "TotalPersonalScoreAwarded": 60
      },
      {
        "NameId": 601966503,
        "Count": 251,
        "TotalPersonalScoreAwarded": 300
      },
      {
        "NameId": 555570945,
        "Count": 228,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 3472794399,
        "Count": 3,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 249491819,
        "Count": 39,
        "TotalPersonalScoreAwarded": -100
      },
      {
        "NameId": 3107879375,
        "Count": 10,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 911992497,
        "Count": 12,
        "TotalPersonalScoreAwarded": -100
      },
      {
        "NameId": 4254982885,
        "Count": 11,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 1614285349,
        "Count": 8,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 1059880024,
        "Count": 1,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 3150095814,
        "Count": 2,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 340198991,
        "Count": 2905,
        "TotalPersonalScoreAwarded": 275
      },
      {
        "NameId": 1032565232,
        "Count": 269,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 2188620691,
        "Count": 18,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 2801241965,
        "Count": 8,
        "TotalPersonalScoreAwarded": 150
      },
      {
        "NameId": 522435689,
        "Count": 17,
        "TotalPersonalScoreAwarded": 1000
      },
      {
        "NameId": 2408971842,
        "Count": 20,
        "TotalPersonalScoreAwarded": 200
      },
      {
        "NameId": 665081740,
        "Count": 12,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 757037588,
        "Count": 102,
        "TotalPersonalScoreAwarded": 600
      },
      {
        "NameId": 4026987576,
        "Count": 39,
        "TotalPersonalScoreAwarded": 375
      },
      {
        "NameId": 2106274556,
        "Count": 2,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 221060588,
        "Count": 3,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 2107631925,
        "Count": 1,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 3243589708,
        "Count": 3,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 2008690931,
        "Count": 1,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 1267013266,
        "Count": 13,
        "TotalPersonalScoreAwarded": 20
      },
      {
        "NameId": 3454330054,
        "Count": 1,
        "TotalPersonalScoreAwarded": 100
      },
      {
        "NameId": 4130011565,
        "Count": 4,
        "TotalPersonalScoreAwarded": 200
      },
      {
        "NameId": 1117301492,
        "Count": 1,
        "TotalPersonalScoreAwarded": 50
      },
      {
        "NameId": 4247243561,
        "Count": 1,
        "TotalPersonalScoreAwarded": 25
      },
      {
        "NameId": 1825517751,
        "Count": 1,
        "TotalPersonalScoreAwarded": 50
      }
    ],
    "Spawns": 26972,
    "ObjectivesCompleted": 0
  },
  "CaptureTheFlagStats": {
    "FlagCaptureAssists": 228,
    "FlagCaptures": 251,
    "FlagCarriersKilled": 305,
    "FlagGrabs": 2881,
    "FlagReturnersKilled": 201,
    "FlagReturns": 412,
    "FlagSecures": 1972,
    "FlagSteals": 824,
    "KillsAsFlagCarrier": 17,
    "KillsAsFlagReturner": 73,
    "TimeAsFlagCarrier": "PT2H24M20.1S"
  },
  "EliminationStats": {
    "AlliesRevived": 0,
    "EliminationAssists": 6,
    "Eliminations": 20,
    "EnemyRevivesDenied": 0,
    "Executions": 17,
    "KillsAsLastPlayerStanding": 0,
    "LastPlayersStandingKilled": 1,
    "RoundsSurvived": 1,
    "TimesRevivedByAlly": 0
  },
  "ExtractionStats": {
    "SuccessfulExtractions": 1,
    "ExtractionConversionsDenied": 1,
    "ExtractionConversionsCompleted": 1,
    "ExtractionInitiationsDenied": 0,
    "ExtractionInitiationsCompleted": 1
  },
  "OddballStats": {
    "KillsAsSkullCarrier": 29,
    "LongestTimeAsSkullCarrier": "PT1M39.9S",
    "SkullCarriersKilled": 578,
    "SkullGrabs": 285,
    "TimeAsSkullCarrier": "PT5H14M5.2S",
    "SkullScoringTicks": 17698
  },
  "ZonesStats": {
    "ZoneCaptures": 4039,
    "ZoneDefensiveKills": 1496,
    "ZoneOffensiveKills": 2026,
    "ZoneSecures": 1065,
    "TotalZoneOccupationTime": "PT13H38M10.8S",
    "ZoneScoringTicks": 14486
  },
  "StockpileStats": {
    "KillsAsPowerSeedCarrier": 0,
    "PowerSeedCarriersKilled": 6,
    "PowerSeedsDeposited": 18,
    "PowerSeedsStolen": 2,
    "TimeAsPowerSeedCarrier": "PT6M45.8S",
    "TimeAsPowerSeedDriver": "PT0S"
  },
  "PvpStats": {
    "Kills": 2659,
    "Deaths": 2731,
    "Assists": 1295
  }
}
```

---
## PlaylistCSRSnapshots - CSR History

| Timestamp | Playlist | CSR Data |
|---|---|---|
| 2026-05-11T22:10:27.666+09:00 | Ranked Arena | [See below](#csr-2026-05-11T22:10:27.666+09:00) |
| 2026-05-11T22:10:27.666+09:00 | Ranked Arena | [See below](#csr-2026-05-11T22:10:27.666+09:00) |
| 2026-05-11T22:10:27.666+09:00 | Ranked Arena | [See below](#csr-2026-05-11T22:10:27.666+09:00) |
| 2026-05-11T22:10:39.598+09:00 | Ranked Doubles | [See below](#csr-2026-05-11T22:10:39.598+09:00) |
| 2026-05-11T22:10:47.119+09:00 | Ranked Snipers | [See below](#csr-2026-05-11T22:10:47.119+09:00) |
| 2026-05-11T22:10:48.975+09:00 | Ranked Slayer | [See below](#csr-2026-05-11T22:10:48.975+09:00) |
| 2026-05-12T15:00:18.297+09:00 | Ranked Arena | [See below](#csr-2026-05-12T15:00:18.297+09:00) |
| 2026-05-12T15:00:18.297+09:00 | Ranked Arena | [See below](#csr-2026-05-12T15:00:18.297+09:00) |
| 2026-05-12T15:00:18.297+09:00 | Ranked Arena | [See below](#csr-2026-05-12T15:00:18.297+09:00) |
| 2026-05-12T15:00:26.855+09:00 | Ranked Doubles | [See below](#csr-2026-05-12T15:00:26.855+09:00) |
| 2026-05-12T15:00:33.540+09:00 | Ranked Snipers | [See below](#csr-2026-05-12T15:00:33.540+09:00) |
| 2026-05-12T15:00:34.973+09:00 | Ranked Slayer | [See below](#csr-2026-05-12T15:00:34.973+09:00) |
| 2026-05-13T03:58:33.034+09:00 | Ranked Arena | [See below](#csr-2026-05-13T03:58:33.034+09:00) |
| 2026-05-13T03:58:33.034+09:00 | Ranked Arena | [See below](#csr-2026-05-13T03:58:33.034+09:00) |
| 2026-05-13T03:58:33.034+09:00 | Ranked Arena | [See below](#csr-2026-05-13T03:58:33.034+09:00) |
| 2026-05-13T03:58:43.770+09:00 | Ranked Doubles | [See below](#csr-2026-05-13T03:58:43.770+09:00) |
| 2026-05-13T03:58:51.801+09:00 | Ranked Snipers | [See below](#csr-2026-05-13T03:58:51.801+09:00) |
| 2026-05-13T03:58:53.486+09:00 | Ranked Slayer | [See below](#csr-2026-05-13T03:58:53.486+09:00) |
| 2026-05-13T19:19:51.792+09:00 | Ranked Arena | [See below](#csr-2026-05-13T19:19:51.792+09:00) |
| 2026-05-13T19:19:51.792+09:00 | Ranked Arena | [See below](#csr-2026-05-13T19:19:51.792+09:00) |
| 2026-05-13T19:19:51.792+09:00 | Ranked Arena | [See below](#csr-2026-05-13T19:19:51.792+09:00) |
| 2026-05-13T19:20:00.415+09:00 | Ranked Doubles | [See below](#csr-2026-05-13T19:20:00.415+09:00) |
| 2026-05-13T19:20:06.853+09:00 | Ranked Snipers | [See below](#csr-2026-05-13T19:20:06.853+09:00) |
| 2026-05-13T19:20:08.590+09:00 | Ranked Slayer | [See below](#csr-2026-05-13T19:20:08.590+09:00) |

<a name='csr-2026-05-11T22:10:27.666+09:00'></a>
### CSR at 2026-05-11T22:10:27.666+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1020,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-11T22:10:27.666+09:00'></a>
### CSR at 2026-05-11T22:10:27.666+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1020,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-11T22:10:27.666+09:00'></a>
### CSR at 2026-05-11T22:10:27.666+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1020,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-11T22:10:39.598+09:00'></a>
### CSR at 2026-05-11T22:10:39.598+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1083,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1083,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1153,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1150,
        "SubTier": 5,
        "NextTier": "Diamond",
        "NextTierStart": 1200,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-11T22:10:47.119+09:00'></a>
### CSR at 2026-05-11T22:10:47.119+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": -1,
        "MeasurementMatchesRemaining": 2,
        "Tier": "",
        "TierStart": 0,
        "SubTier": 0,
        "NextTier": "",
        "NextTierStart": 0,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": -1,
        "MeasurementMatchesRemaining": 2,
        "Tier": "",
        "TierStart": 0,
        "SubTier": 0,
        "NextTier": "",
        "NextTierStart": 0,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1160,
        "MeasurementMatchesRemaining": 2,
        "Tier": "Platinum",
        "TierStart": 1150,
        "SubTier": 5,
        "NextTier": "Diamond",
        "NextTierStart": 1200,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-11T22:10:48.975+09:00'></a>
### CSR at 2026-05-11T22:10:48.975+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1407,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1400,
        "SubTier": 4,
        "NextTier": "Diamond",
        "NextTierStart": 1450,
        "NextSubTier": 5,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1407,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1400,
        "SubTier": 4,
        "NextTier": "Diamond",
        "NextTierStart": 1450,
        "NextSubTier": 5,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1407,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1400,
        "SubTier": 4,
        "NextTier": "Diamond",
        "NextTierStart": 1450,
        "NextSubTier": 5,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-12T15:00:18.297+09:00'></a>
### CSR at 2026-05-12T15:00:18.297+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1023,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-12T15:00:18.297+09:00'></a>
### CSR at 2026-05-12T15:00:18.297+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1023,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-12T15:00:18.297+09:00'></a>
### CSR at 2026-05-12T15:00:18.297+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1023,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-12T15:00:26.855+09:00'></a>
### CSR at 2026-05-12T15:00:26.855+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1083,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1083,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1153,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1150,
        "SubTier": 5,
        "NextTier": "Diamond",
        "NextTierStart": 1200,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-12T15:00:33.540+09:00'></a>
### CSR at 2026-05-12T15:00:33.540+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": -1,
        "MeasurementMatchesRemaining": 2,
        "Tier": "",
        "TierStart": 0,
        "SubTier": 0,
        "NextTier": "",
        "NextTierStart": 0,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": -1,
        "MeasurementMatchesRemaining": 2,
        "Tier": "",
        "TierStart": 0,
        "SubTier": 0,
        "NextTier": "",
        "NextTierStart": 0,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1160,
        "MeasurementMatchesRemaining": 2,
        "Tier": "Platinum",
        "TierStart": 1150,
        "SubTier": 5,
        "NextTier": "Diamond",
        "NextTierStart": 1200,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-12T15:00:34.973+09:00'></a>
### CSR at 2026-05-12T15:00:34.973+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1397,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1350,
        "SubTier": 3,
        "NextTier": "Diamond",
        "NextTierStart": 1400,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1418,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1400,
        "SubTier": 4,
        "NextTier": "Diamond",
        "NextTierStart": 1450,
        "NextSubTier": 5,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1418,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1400,
        "SubTier": 4,
        "NextTier": "Diamond",
        "NextTierStart": 1450,
        "NextSubTier": 5,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T03:58:33.034+09:00'></a>
### CSR at 2026-05-13T03:58:33.034+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1017,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T03:58:33.034+09:00'></a>
### CSR at 2026-05-13T03:58:33.034+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1017,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T03:58:33.034+09:00'></a>
### CSR at 2026-05-13T03:58:33.034+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1017,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T03:58:43.770+09:00'></a>
### CSR at 2026-05-13T03:58:43.770+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1083,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1083,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1153,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1150,
        "SubTier": 5,
        "NextTier": "Diamond",
        "NextTierStart": 1200,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T03:58:51.801+09:00'></a>
### CSR at 2026-05-13T03:58:51.801+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": -1,
        "MeasurementMatchesRemaining": 2,
        "Tier": "",
        "TierStart": 0,
        "SubTier": 0,
        "NextTier": "",
        "NextTierStart": 0,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": -1,
        "MeasurementMatchesRemaining": 2,
        "Tier": "",
        "TierStart": 0,
        "SubTier": 0,
        "NextTier": "",
        "NextTierStart": 0,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1160,
        "MeasurementMatchesRemaining": 2,
        "Tier": "Platinum",
        "TierStart": 1150,
        "SubTier": 5,
        "NextTier": "Diamond",
        "NextTierStart": 1200,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T03:58:53.486+09:00'></a>
### CSR at 2026-05-13T03:58:53.486+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1375,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1350,
        "SubTier": 3,
        "NextTier": "Diamond",
        "NextTierStart": 1400,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1418,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1400,
        "SubTier": 4,
        "NextTier": "Diamond",
        "NextTierStart": 1450,
        "NextSubTier": 5,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1418,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1400,
        "SubTier": 4,
        "NextTier": "Diamond",
        "NextTierStart": 1450,
        "NextSubTier": 5,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T19:19:51.792+09:00'></a>
### CSR at 2026-05-13T19:19:51.792+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1017,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T19:19:51.792+09:00'></a>
### CSR at 2026-05-13T19:19:51.792+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1017,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T19:19:51.792+09:00'></a>
### CSR at 2026-05-13T19:19:51.792+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1017,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1000,
        "SubTier": 2,
        "NextTier": "Platinum",
        "NextTierStart": 1050,
        "NextSubTier": 3,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1090,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1588,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Onyx",
        "TierStart": 1500,
        "SubTier": 0,
        "NextTier": "Onyx",
        "NextTierStart": 1500,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T19:20:00.415+09:00'></a>
### CSR at 2026-05-13T19:20:00.415+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1083,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1083,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1050,
        "SubTier": 3,
        "NextTier": "Platinum",
        "NextTierStart": 1100,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1153,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Platinum",
        "TierStart": 1150,
        "SubTier": 5,
        "NextTier": "Diamond",
        "NextTierStart": 1200,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T19:20:06.853+09:00'></a>
### CSR at 2026-05-13T19:20:06.853+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": -1,
        "MeasurementMatchesRemaining": 2,
        "Tier": "",
        "TierStart": 0,
        "SubTier": 0,
        "NextTier": "",
        "NextTierStart": 0,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": -1,
        "MeasurementMatchesRemaining": 2,
        "Tier": "",
        "TierStart": 0,
        "SubTier": 0,
        "NextTier": "",
        "NextTierStart": 0,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1160,
        "MeasurementMatchesRemaining": 2,
        "Tier": "Platinum",
        "TierStart": 1150,
        "SubTier": 5,
        "NextTier": "Diamond",
        "NextTierStart": 1200,
        "NextSubTier": 0,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

<a name='csr-2026-05-13T19:20:08.590+09:00'></a>
### CSR at 2026-05-13T19:20:08.590+09:00
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 0,
    "Result": {
      "Current": {
        "Value": 1383,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1350,
        "SubTier": 3,
        "NextTier": "Diamond",
        "NextTierStart": 1400,
        "NextSubTier": 4,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "SeasonMax": {
        "Value": 1418,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1400,
        "SubTier": 4,
        "NextTier": "Diamond",
        "NextTierStart": 1450,
        "NextSubTier": 5,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      },
      "AllTimeMax": {
        "Value": 1418,
        "MeasurementMatchesRemaining": 0,
        "Tier": "Diamond",
        "TierStart": 1400,
        "SubTier": 4,
        "NextTier": "Diamond",
        "NextTierStart": 1450,
        "NextSubTier": 5,
        "InitialMeasurementMatches": 5,
        "DemotionProtectionMatchesRemaining": 0,
        "InitialDemotionProtectionMatches": 3
      }
    }
  }
]
```

---
## MatchStats - Complete Match Detail (Sample 1)

### MatchId: `86c0de94-b42f-4926-ac40-19c39d3b0284`

### MatchInfo
```json
{
  "StartTime": "2026-05-06T14:58:55.16Z",
  "EndTime": "2026-05-06T15:03:38.261Z",
  "Duration": "PT4M43.0870026S",
  "LifecycleMode": 1,
  "GameVariantCategory": 6,
  "LevelId": "c7b7baf0-f206-11e4-ae9a-24be05e24f7e",
  "MapVariant": {
    "AssetKind": 2,
    "AssetId": "29c99861-84c6-4402-ba09-7ab4b442bf04",
    "VersionId": "28f9dd56-ce15-418b-ac96-e35461646a03"
  },
  "UgcGameVariant": {
    "AssetKind": 6,
    "AssetId": "fa4dc960-5240-4aaa-8486-eb6bc0aa95aa",
    "VersionId": "628d8504-fc36-4b08-8743-8d7433e867a4"
  },
  "ClearanceId": "d22ce0c2-d635-43e7-8d7f-4506a43b20f3",
  "Playlist": null,
  "PlaylistExperience": null,
  "PlaylistMapModePair": null,
  "SeasonId": null,
  "PlayableDuration": "PT4M43.094S",
  "TeamsEnabled": true,
  "TeamScoringEnabled": true,
  "GameplayInteraction": 1
}
```

### Teams
```json
[
  {
    "TeamId": 0,
    "Outcome": 3,
    "Rank": 2,
    "Stats": {
      "CoreStats": {
        "Score": 12,
        "PersonalScore": 1200,
        "RoundsWon": 0,
        "RoundsLost": 1,
        "RoundsTied": 0,
        "Kills": 12,
        "Deaths": 25,
        "Assists": 0,
        "KDA": -13.0,
        "Suicides": 0,
        "Betrayals": 0,
        "AverageLifeDuration": "PT9.5S",
        "GrenadeKills": 1,
        "HeadshotKills": 11,
        "MeleeKills": 0,
        "PowerWeaponKills": 4,
        "ShotsFired": 145,
        "ShotsHit": 67,
        "Accuracy": 46.2,
        "DamageDealt": 4167,
        "DamageTaken": 5878,
        "CalloutAssists": 0,
        "VehicleDestroys": 0,
        "DriverAssists": 0,
        "Hijacks": 0,
        "EmpAssists": 0,
        "MaxKillingSpree": 3,
        "Medals": [
          {
            "NameId": 4229934157,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 622331684,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 2123530881,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 1512363953,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 3233952928,
            "Count": 2,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 2602963073,
            "Count": 3,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 2852571933,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          }
        ],
        "PersonalScores": [
          {
            "NameId": 1024030246,
            "Count": 12,
            "TotalPersonalScoreAwarded": 1200
          }
        ],
        "DeprecatedDamageDealt": 4167.0,
        "DeprecatedDamageTaken": 5878.0,
        "Spawns": 25,
        "ObjectivesCompleted": 0
      },
      "PvpStats": {
        "Kills": 12,
        "Deaths": 25,
        "Assists": 0,
        "KDA": -13.0
      }
    }
  },
  {
    "TeamId": 1,
    "Outcome": 2,
    "Rank": 1,
    "Stats": {
      "CoreStats": {
        "Score": 25,
        "PersonalScore": 2500,
        "RoundsWon": 1,
        "RoundsLost": 0,
        "RoundsTied": 0,
        "Kills": 25,
        "Deaths": 12,
        "Assists": 0,
        "KDA": 13.0,
        "Suicides": 0,
        "Betrayals": 0,
        "AverageLifeDuration": "PT19.2S",
        "GrenadeKills": 3,
        "HeadshotKills": 17,
        "MeleeKills": 2,
        "PowerWeaponKills": 3,
        "ShotsFired": 160,
        "ShotsHit": 91,
        "Accuracy": 56.87,
        "DamageDealt": 5878,
        "DamageTaken": 4167,
        "CalloutAssists": 0,
        "VehicleDestroys": 0,
        "DriverAssists": 0,
        "Hijacks": 0,
        "EmpAssists": 0,
        "MaxKillingSpree": 6,
        "Medals": [
          {
            "NameId": 2852571933,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 2780740615,
            "Count": 2,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 2602963073,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 2123530881,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 3655682764,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 622331684,
            "Count": 2,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 4229934157,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 2063152177,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 1477806194,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          },
          {
            "NameId": 1169390319,
            "Count": 1,
            "TotalPersonalScoreAwarded": 0
          }
        ],
        "PersonalScores": [
          {
            "NameId": 1024030246,
            "Count": 25,
            "TotalPersonalScoreAwarded": 2500
          }
        ],
        "DeprecatedDamageDealt": 5878.0,
        "DeprecatedDamageTaken": 4167.0,
        "Spawns": 13,
        "ObjectivesCompleted": 0
      },
      "PvpStats": {
        "Kills": 25,
        "Deaths": 12,
        "Assists": 0,
        "KDA": 13.0
      }
    }
  }
]
```

### Players
```json
[
  {
    "PlayerId": "xuid({YOUR_XUID})",
    "PlayerType": 1,
    "BotAttributes": null,
    "LastTeamId": 0,
    "Outcome": 3,
    "Rank": 2,
    "ParticipationInfo": {
      "FirstJoinedTime": "2026-05-06T14:58:55.161Z",
      "LastLeaveTime": null,
      "PresentAtBeginning": true,
      "JoinedInProgress": false,
      "LeftInProgress": false,
      "PresentAtCompletion": true,
      "TimePlayed": "PT4M43.094S",
      "ConfirmedParticipation": null
    },
    "PlayerTeamStats": [
      {
        "TeamId": 0,
        "Stats": {
          "CoreStats": {
            "Score": 12,
            "PersonalScore": 1200,
            "RoundsWon": 0,
            "RoundsLost": 1,
            "RoundsTied": 0,
            "Kills": 12,
            "Deaths": 25,
            "Assists": 0,
            "KDA": -13.0,
            "Suicides": 0,
            "Betrayals": 0,
            "AverageLifeDuration": "PT9.5S",
            "GrenadeKills": 1,
            "HeadshotKills": 11,
            "MeleeKills": 0,
            "PowerWeaponKills": 4,
            "ShotsFired": 145,
            "ShotsHit": 67,
            "Accuracy": 46.2,
            "DamageDealt": 4167,
            "DamageTaken": 5878,
            "CalloutAssists": 0,
            "VehicleDestroys": 0,
            "DriverAssists": 0,
            "Hijacks": 0,
            "EmpAssists": 0,
            "MaxKillingSpree": 3,
            "Medals": [
              {
                "NameId": 4229934157,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 622331684,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 2123530881,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 1512363953,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 3233952928,
                "Count": 2,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 2602963073,
                "Count": 3,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 2852571933,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              }
            ],
            "PersonalScores": [
              {
                "NameId": 1024030246,
                "Count": 12,
                "TotalPersonalScoreAwarded": 1200
              }
            ],
            "DeprecatedDamageDealt": 4167.0,
            "DeprecatedDamageTaken": 5878.0,
            "Spawns": 25,
            "ObjectivesCompleted": 0
          },
          "PvpStats": {
            "Kills": 12,
            "Deaths": 25,
            "Assists": 0,
            "KDA": -13.0
          }
        }
      }
    ]
  },
  {
    "PlayerId": "xuid(2533274962782816)",
    "PlayerType": 1,
    "BotAttributes": null,
    "LastTeamId": 1,
    "Outcome": 2,
    "Rank": 1,
    "ParticipationInfo": {
      "FirstJoinedTime": "2026-05-06T14:58:55.173Z",
      "LastLeaveTime": null,
      "PresentAtBeginning": true,
      "JoinedInProgress": false,
      "LeftInProgress": false,
      "PresentAtCompletion": true,
      "TimePlayed": "PT4M43.094S",
      "ConfirmedParticipation": null
    },
    "PlayerTeamStats": [
      {
        "TeamId": 1,
        "Stats": {
          "CoreStats": {
            "Score": 25,
            "PersonalScore": 2500,
            "RoundsWon": 1,
            "RoundsLost": 0,
            "RoundsTied": 0,
            "Kills": 25,
            "Deaths": 12,
            "Assists": 0,
            "KDA": 13.0,
            "Suicides": 0,
            "Betrayals": 0,
            "AverageLifeDuration": "PT19.2S",
            "GrenadeKills": 3,
            "HeadshotKills": 17,
            "MeleeKills": 2,
            "PowerWeaponKills": 3,
            "ShotsFired": 160,
            "ShotsHit": 91,
            "Accuracy": 56.87,
            "DamageDealt": 5878,
            "DamageTaken": 4167,
            "CalloutAssists": 0,
            "VehicleDestroys": 0,
            "DriverAssists": 0,
            "Hijacks": 0,
            "EmpAssists": 0,
            "MaxKillingSpree": 6,
            "Medals": [
              {
                "NameId": 2852571933,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 2780740615,
                "Count": 2,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 2602963073,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 2123530881,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 3655682764,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 622331684,
                "Count": 2,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 4229934157,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 2063152177,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 1477806194,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              },
              {
                "NameId": 1169390319,
                "Count": 1,
                "TotalPersonalScoreAwarded": 0
              }
            ],
            "PersonalScores": [
              {
                "NameId": 1024030246,
                "Count": 25,
                "TotalPersonalScoreAwarded": 2500
              }
            ],
            "DeprecatedDamageDealt": 5878.0,
            "DeprecatedDamageTaken": 4167.0,
            "Spawns": 13,
            "ObjectivesCompleted": 0
          },
          "PvpStats": {
            "Kills": 25,
            "Deaths": 12,
            "Assists": 0,
            "KDA": 13.0
          }
        }
      }
    ]
  }
]
```

---
## PlayerMatchStats - Sample (Self CSR Data)

### MatchId: `86c0de94-b42f-4926-ac40-19c39d3b0284`

**StartTime**: 2026-05-06T14:58:55.16Z
**PlayableDuration**: PT4M43.094S

### PlayerStats (CSR Array)
```json
[
  {
    "Id": "xuid({YOUR_XUID})",
    "ResultCode": 1,
    "Result": {
      "TeamMmr": 0.0,
      "RankRecap": {
        "PreMatchCsr": {
          "Value": 0,
          "MeasurementMatchesRemaining": 0,
          "Tier": "",
          "TierStart": 0,
          "SubTier": 0,
          "NextTier": "",
          "NextTierStart": 0,
          "NextSubTier": 0,
          "InitialMeasurementMatches": 0,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 0
        },
        "PostMatchCsr": {
          "Value": 0,
          "MeasurementMatchesRemaining": 0,
          "Tier": "",
          "TierStart": 0,
          "SubTier": 0,
          "NextTier": "",
          "NextTierStart": 0,
          "NextSubTier": 0,
          "InitialMeasurementMatches": 0,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 0
        }
      },
      "StatPerformances": {},
      "TeamId": 0,
      "TeamMmrs": {},
      "RankedRewards": null,
      "Counterfactuals": null
    }
  },
  {
    "Id": "xuid(2533274962782816)",
    "ResultCode": 1,
    "Result": {
      "TeamMmr": 0.0,
      "RankRecap": {
        "PreMatchCsr": {
          "Value": 0,
          "MeasurementMatchesRemaining": 0,
          "Tier": "",
          "TierStart": 0,
          "SubTier": 0,
          "NextTier": "",
          "NextTierStart": 0,
          "NextSubTier": 0,
          "InitialMeasurementMatches": 0,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 0
        },
        "PostMatchCsr": {
          "Value": 0,
          "MeasurementMatchesRemaining": 0,
          "Tier": "",
          "TierStart": 0,
          "SubTier": 0,
          "NextTier": "",
          "NextTierStart": 0,
          "NextSubTier": 0,
          "InitialMeasurementMatches": 0,
          "DemotionProtectionMatchesRemaining": 0,
          "InitialDemotionProtectionMatches": 0
        }
      },
      "StatPerformances": {},
      "TeamId": 0,
      "TeamMmrs": {},
      "RankedRewards": null,
      "Counterfactuals": null
    }
  }
]
```

---
## Maps - All Entries

| AssetId | PublicName | Description |
|---|---|---|
| 929ff1e7-308f-4780-baf3-8c8b5cc26324 | 1V1 BR Tournament | set it up with 1 kill per round FFA with multiple rounds. I  |
| 6c8f6bdb-d4e8-456e-a344-87278d273a60 | AIMBOTZ V2 | A new and improved verson of AIMBOTZ, inspired by the counte |
| f95073b3-e47a-4c12-a65e-df0229d08269 | Aim Training Targets | Refine your aim against randomly spawning targets. Use with  |
| 023507d1-7566-458d-b3d7-31627c40c01d | Apostle | Silence fills the empty grave... |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 33c0766c-ef15-48f8-b298-34aba5bff3b4 | Aquarius | Aquarius Terraforming Solutions: Industry leader in returnin |
| 667072ae-ba00-4414-adda-8203e8c49295 | Aquarius - Ranked | Aquarius Terraforming Solutions: Industry leader in returnin |
| dd600260-d91c-4d77-9990-3f35873c90a1 | Argyle | An incredible feat of engineering. |
| dd600260-d91c-4d77-9990-3f35873c90a1 | Argyle | An incredible feat of engineering. |
| dd600260-d91c-4d77-9990-3f35873c90a1 | Argyle | An incredible feat of engineering. |
| dd600260-d91c-4d77-9990-3f35873c90a1 | Argyle | An incredible feat of engineering. |
| dd600260-d91c-4d77-9990-3f35873c90a1 | Argyle | An incredible feat of engineering. |
| dd600260-d91c-4d77-9990-3f35873c90a1 | Argyle | An incredible feat of engineering. |
| dd600260-d91c-4d77-9990-3f35873c90a1 | Argyle | An incredible feat of engineering. |
| dd600260-d91c-4d77-9990-3f35873c90a1 | Argyle | An incredible feat of engineering. |
| 78677080-db7a-429e-84fe-f041d8342c37 | Argyle - Ranked | An incredible feat of engineering. |
| 98321723-6e89-4ec0-8bd2-b313cfa620b1 | BRT | 1v1 BR Training |
| 5447bbbf-7ae0-4761-ad22-d6dd3364c646 | BRT | 1v1 BR Training |
| 5447bbbf-7ae0-4761-ad22-d6dd3364c646 | BRT | 1v1 BR Training |
| 86ef67f3-e01c-447f-a4e9-f66399e1014d | BRT 1.1 | 1v1 BR Training |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 9a01ad89-1f3f-4f19-bde5-65a93ae9cff1 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 29c99861-84c6-4402-ba09-7ab4b442bf04 | BRT 1.2 | 1v1 BR Training. Update:Adjustments were made to allow the g |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 298d5036-cd43-47b3-a4bd-31e127566593 | Bazaar | Dusty streets and double doors. |
| 61cbf45f-6fdb-4dce-9ead-baea363c9b73 | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 53136ad9-0fd6-4271-8752-31d114b9561e | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 53136ad9-0fd6-4271-8752-31d114b9561e | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 53136ad9-0fd6-4271-8752-31d114b9561e | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 53136ad9-0fd6-4271-8752-31d114b9561e | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 53136ad9-0fd6-4271-8752-31d114b9561e | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 53136ad9-0fd6-4271-8752-31d114b9561e | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 53136ad9-0fd6-4271-8752-31d114b9561e | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 53136ad9-0fd6-4271-8752-31d114b9561e | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 53136ad9-0fd6-4271-8752-31d114b9561e | Behemoth | Buried for millennia, this ancient structure rises from bene |
| 4bf46ecf-606f-4fb8-a767-2ad6e982831b | Bot snipe shooting gallery | Mark a location to spawn new sniper. Add bots to team cobra. |
| e6cbfe01-665b-4a8c-bf3a-d63a65a7c890 | Breaker | Plasma Beam. 6500 Terawatts, 25000 degrees Centigrade. |
| e6cbfe01-665b-4a8c-bf3a-d63a65a7c890 | Breaker | Plasma Beam. 6500 Terawatts, 25000 degrees Centigrade. |
| e6cbfe01-665b-4a8c-bf3a-d63a65a7c890 | Breaker | Plasma Beam. 6500 Terawatts, 25000 degrees Centigrade. |
| e6cbfe01-665b-4a8c-bf3a-d63a65a7c890 | Breaker | Plasma Beam. 6500 Terawatts, 25000 degrees Centigrade. |
| e6cbfe01-665b-4a8c-bf3a-d63a65a7c890 | Breaker |  |
| 0f191b95-90ca-4d4b-88f6-f6c1d90045cb | CTF Warmup AW | CTF Warmup V1. Should be played with the CTF Warm Up AW game |
| a26678d4-5a24-44bb-8158-bbed37b4afda | CTF Warmup AW | CTF Warmup V1. Should be played with the CTF Warm Up AW game |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| e859cf75-9b8a-429a-91be-2376681c8537 | Catalyst | Spent shells rain like water in this ancient sanctuary. |
| 7ecaa689-afca-44a6-a6a7-9030246a7d8a | Caution | Functional 1v1-4v4 Slayer Map (Not Arted) |
| fc1ced39-128b-439d-9b44-4710225090f3 | Chasm | Mind the gap. |
| fc1ced39-128b-439d-9b44-4710225090f3 | Chasm | Mind the gap. |
| fc1ced39-128b-439d-9b44-4710225090f3 | Chasm | Mind the gap. |
| fc1ced39-128b-439d-9b44-4710225090f3 | Chasm | Mind the gap. |
| fc1ced39-128b-439d-9b44-4710225090f3 | Chasm | Mind the gap. |
| 81274d6f-6a94-425a-a16e-3bdb1e2eea9d | Cliffhanger | High altitude. Highly classified. |
| 81274d6f-6a94-425a-a16e-3bdb1e2eea9d | Cliffhanger | High altitude. Highly classified. |
| 81274d6f-6a94-425a-a16e-3bdb1e2eea9d | Cliffhanger | High altitude. Highly classified. |
| 81274d6f-6a94-425a-a16e-3bdb1e2eea9d | Cliffhanger | High altitude. Highly classified. |
| 81274d6f-6a94-425a-a16e-3bdb1e2eea9d | Cliffhanger | High altitude. Highly classified. |
| 08607bf4-6abe-4a5b-9547-290a6cc1433e | Deadlock | UNSC forces have yet to breach this Banished encampment. |
| 08607bf4-6abe-4a5b-9547-290a6cc1433e | Deadlock | UNSC forces have yet to breach this Banished encampment. |
| 08607bf4-6abe-4a5b-9547-290a6cc1433e | Deadlock | UNSC forces have yet to breach this Banished encampment. |
| 08607bf4-6abe-4a5b-9547-290a6cc1433e | Deadlock | UNSC forces have yet to breach this Banished encampment. |
| 08607bf4-6abe-4a5b-9547-290a6cc1433e | Deadlock | UNSC forces have yet to breach this Banished encampment. |
| 08607bf4-6abe-4a5b-9547-290a6cc1433e | Deadlock | UNSC forces have yet to breach this Banished encampment. |
| d39600e2-3c35-4a3a-bdf5-7b3cbdde98e1 | Detachment | No complex riddle, just stick to the middle. |
| d39600e2-3c35-4a3a-bdf5-7b3cbdde98e1 | Detachment | No complex riddle, just stick to the middle. |
| d39600e2-3c35-4a3a-bdf5-7b3cbdde98e1 | Detachment | No complex riddle, just stick to the middle. |
| d39600e2-3c35-4a3a-bdf5-7b3cbdde98e1 | Detachment | No complex riddle, just stick to the middle. |
| d035fc3e-f298-4c14-9487-465be2e1dc1f | Empyrean | Sleepless nights, timeless fights |
| d035fc3e-f298-4c14-9487-465be2e1dc1f | Empyrean | Sleepless nights, timeless fights |
| d035fc3e-f298-4c14-9487-465be2e1dc1f | Empyrean | Sleepless nights, timeless fights |
| d035fc3e-f298-4c14-9487-465be2e1dc1f | Empyrean | Sleepless nights, timeless fights |
| d035fc3e-f298-4c14-9487-465be2e1dc1f | Empyrean | Sleepless nights, timeless fights |
| d035fc3e-f298-4c14-9487-465be2e1dc1f | Empyrean | Sleepless nights, timeless fights |
| d035fc3e-f298-4c14-9487-465be2e1dc1f | Empyrean | Sleepless nights, timeless fights |
| d035fc3e-f298-4c14-9487-465be2e1dc1f | Empyrean | Sleepless nights, timeless fights |
| 70dd38c5-2eb7-4db3-8901-0dfca292ff18 | Empyrean - Ranked | Sleepless nights, timeless fights |
| db2b5f9c-9895-4f73-9d57-44f9b191f3cf | Forbidden | These halls hide history of both triumph and terror. |
| 5c215079-c34d-4d25-b86a-435e35edf188 | Forbidden - Ranked | These halls hide history of both triumph and terror. |
| a54808fb-9bf5-432a-a3c3-f76cbea944c1 | Fortress - Ranked | Battles of long ago echo throughout the valley. |
| 4f196016-0101-4844-8358-2504f7c44656 | Fragmentation | These beacons are no stranger to explosive conflict. |
| 4f196016-0101-4844-8358-2504f7c44656 | Fragmentation | These beacons are no stranger to explosive conflict. |
| 4f196016-0101-4844-8358-2504f7c44656 | Fragmentation | These beacons are no stranger to explosive conflict. |
| 4f196016-0101-4844-8358-2504f7c44656 | Fragmentation | These beacons are no stranger to explosive conflict. |
| 4f196016-0101-4844-8358-2504f7c44656 | Fragmentation | These beacons are no stranger to explosive conflict. |
| 4f196016-0101-4844-8358-2504f7c44656 | Fragmentation | These beacons are no stranger to explosive conflict. |
| fa399f2a-9fea-4108-9a20-e2ffceb68495 | Halo Shipment MW19! Most recent | Halo Shipment MW19 Most recent SLAYER! |
| c494ef7c-d203-42a9-9c0f-b3f576334501 | Highpower | High-Power with a high tower. |
| c494ef7c-d203-42a9-9c0f-b3f576334501 | Highpower | High-Power with a high tower. |
| c494ef7c-d203-42a9-9c0f-b3f576334501 | Highpower | High-Power with a high tower. |
| c494ef7c-d203-42a9-9c0f-b3f576334501 | Highpower | High-Power with a high tower. |
| c494ef7c-d203-42a9-9c0f-b3f576334501 | Highpower | High-Power with a high tower. |
| c494ef7c-d203-42a9-9c0f-b3f576334501 | Highpower | High-Power with a high tower. |
| 654dff62-d618-496a-8914-06ab73d991e3 | Interference | Reimagination of the Halo 5's map The Rig with a snowy theme |
| 1a6cfc2e-ec86-48e1-9464-1ce1bff6ed48 | Lattice - Ranked | This abandoned hydroelectric facility holds secrets once bur |
| 56a11b8c-64d1-4537-8893-a9241e4d5b93 | Launch Site | Sabre proving grounds test the limits of human velocity. |
| 56a11b8c-64d1-4537-8893-a9241e4d5b93 | Launch Site | Sabre proving grounds test the limits of human velocity. |
| 56a11b8c-64d1-4537-8893-a9241e4d5b93 | Launch Site | Sabre proving grounds test the limits of human velocity. |
| 56a11b8c-64d1-4537-8893-a9241e4d5b93 | Launch Site | Sabre proving grounds test the limits of human velocity. |
| 56a11b8c-64d1-4537-8893-a9241e4d5b93 | Launch Site | Sabre proving grounds test the limits of human velocity. |
| 56a11b8c-64d1-4537-8893-a9241e4d5b93 | Launch Site | Sabre proving grounds test the limits of human velocity. |
| 56a11b8c-64d1-4537-8893-a9241e4d5b93 | Launch Site | Sabre proving grounds test the limits of human velocity. |
| 56a11b8c-64d1-4537-8893-a9241e4d5b93 | Launch Site | Sabre proving grounds test the limits of human velocity. |
| 56a11b8c-64d1-4537-8893-a9241e4d5b93 | Launch Site | Sabre proving grounds test the limits of human velocity. |
| 6c01f693-c968-4a71-b157-efc35ffcf71f | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| 7de09dad-dd2a-450c-b097-8f2003f6b90f | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| b6aca0c7-8ba7-4066-bf91-693571374c3c | Live Fire | Instructors at the Avery J. Johnson Academy of Military Scie |
| 309253f8-7a75-48ff-83e1-e7fb3db2ac47 | Live Fire - Ranked | Instructors at the Avery J. Johnson Academy of Military Scie |
| cfc9685a-eddb-41c1-be15-0dd5b8b7e066 | Lone Wolf (Survive) | Current Objective: Survive. Lone wolf how you remember it! H |
| c354722b-eea6-481b-a333-9cbbf4b48504 | MLG Octagon | Your favorite Octagon! Play with instant respawn and line-of |
| 6aa0a116-66a6-4242-a1b3-41aa417d6dc6 | Oasis | An ancient gift. A new genesis. |
| 6aa0a116-66a6-4242-a1b3-41aa417d6dc6 | Oasis | An ancient gift. A new genesis. |
| 4c37697d-c876-465b-b46f-230954be6d51 | Octagon | Turn respawn timers down for maximum chaos! |
| ca79065b-6cac-4161-aeb9-e17426ed0c51 | Octagon | Octagon by Jellae! Mid to long ranged weapons recommended! B |
| 96090c8a-0341-400a-becb-d88bb67afd13 | Octagon AW | Octagon Warm Up. Spawns can break if set up as an FFA; use t |
| 08bcab13-ba03-4c95-a5ea-f593c4dc2245 | Octagon AW | Octagon Warm Up. Spawns can break if set up as an FFA; use t |
| 55aa2af0-f274-468d-8c49-c20d8807d40f | Octagon AW | Octagon Warm Up. Spawns can break if set up as an FFA; use t |
| 08bcab13-ba03-4c95-a5ea-f593c4dc2245 | Octagon AW | Octagon Warm Up. Spawns can break if set up as an FFA; use t |
| 08bcab13-ba03-4c95-a5ea-f593c4dc2245 | Octagon AW | Octagon Warm Up. Spawns can break if set up as an FFA; use t |
| 55aa2af0-f274-468d-8c49-c20d8807d40f | Octagon AW | Octagon Warm Up. Spawns can break if set up as an FFA; use t |
| 75cb0f58-21dc-4757-8eb7-c27773697a5a | Octagon HCS 2042 | High above the night sky of New Mombasa, set foot in the Oct |
| 46a8319c-2c63-46ee-9382-788906dcb049 | Origin - Ranked | Forerunner Warrior-Servants tested themselves in this arena  |
| c5ac9f12-660e-4f1a-83e7-2e7536bbcb04 | Perilous | There's something in the water... |
| 2fdb8370-e5ac-4a1a-bdce-a08bc738b9ad | Prism | Deep in the mines of Suban. |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 8420410b-044d-44d7-80b6-98a766c8c39f | Recharge | Power still courses through the walls of this neglected Axys |
| 336b5174-3579-4fd8-b2f0-922e4a5f7628 | Recharge - Ranked | Power still courses through the walls of this neglected Axys |
| f633db01-3989-41d1-b6d4-bf2d220fc619 | Salvation | Those who are condemned, come here seeking salvation. |
| c2c451c8-e0f2-4d4c-a384-4ee826746f85 | Sanctuary | Sanctuary variant for CLB and Slayer modes |
| 486bedea-38d6-4721-8a21-18ecbc0aaefe | Sanctuary | You might want to pack better boots. |
| 1de0bf60-e446-4fb9-970f-d0e54fc6c74a | Serenity - Ranked | Amidst ancient ruins, tranquil waters flow through a symmetr |
| f1cc3b4e-471c-4ec5-b855-1db7d9e6ce42 | Solitude | Not all life finds a way. |
| 4a5e5612-2b2e-4375-a0b3-9335a68815f3 | Solitude - Ranked | Not all life finds a way. |
| 35c4680c-e4d6-43e8-a588-58a0deab980f | Solution |  |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| f0a1760f-0d4a-4bcc-ac7a-e8f9aee331dc | Streets | The tranquility of this Mombasa back alley is pierced by the |
| e23ea388-9bcb-4180-a0dc-fbe987751b9e | Streets - Ranked | The tranquility of this Mombasa back alley is pierced by the |
| 6a1e8432-88ae-4430-8f7d-9ffefc97cc8d | Vacancy - Ranked | You can check out any time you like, but you can never leave |
| 1236fd0c-e812-431a-b0e2-64aa3234d11a | Vagabond |  |

---
## Playlists - All Entries (Deduplicated)

| AssetId | PublicName |
|---|---|
| 3facc347-6e49-40c9-b9e7-503d26092eed | Entrenched |
| 4795cb47-5b32-4c87-98ab-02f12e94ca31 | Extraction 24/7 |
| f6c93ddd-a623-41b1-b9e3-81632ff73cfb | FFA Slayer |
| 4af0b113-8696-4f22-9e09-596d473de933 | Fracture: Tenrai - Fiesta |
| af3cef4b-4837-4d75-b680-0ffe6190009b | Joint Ops |
| 14352c39-a409-4d34-9ded-1c280bb4f868 | Land Grab |
| 0299adc1-f07a-4b6c-8126-0c35ac2fa08d | Last Spartan Standing |
| 90eb5903-0a0d-46b8-973a-8f4fc93edbce | New BTB Unlimited |
| 1b1691dc-d8b9-4b1f-825d-cb1c065184c1 | Quick Play |
| edfef3ac-9cbe-4fa2-b949-8f29deafd483 | Ranked Arena |
| f7f30787-f607-436b-bdec-44c65bc2ecef | Ranked Arena |
| fa5aa2a3-2428-4912-a023-e1eeea7b877c | Ranked Doubles |
| 71734db4-4b8e-4682-9206-62b6eff92582 | Ranked FFA |
| dcb2e24e-05fb-4390-8076-32a0cdb4326e | Ranked Slayer |
| 6233381c-fc96-40b9-b1ff-f6a4de72dd7a | Ranked Snipers |
| 4da919eb-5368-4954-90f5-7e88d678ace7 | Social Skirmish |
| 7f2b4f8f-c2f3-4ad4-a250-b55214fa4111 | Tactical Slayer |
| 7323be09-2523-47c0-9e0d-64af9534ee22 | Team Doubles |
| 325c18a5-d85b-4ba6-b98f-21465d9c19e2 | Team Snipers |

---
## GameVariants - Top 20 by PublicName

| AssetId | PublicName |
|---|---|
| 472b968b-e943-4abe-9516-0296a448d72d | 12345678 |
| 39c18013-26e8-4b58-b28e-1392f3a9ccca | Aim Training Targets |
| f09db8ff-9cda-4cc0-8b29-e8020bf37afe | Aimbotz Unlimited |
| 4d0f6e15-cc3f-46e0-9d06-22de6311c4cb | Arena:Attrition |
| 8650f7e0-1f82-4d45-a127-32dd54df06e5 | Arena:CTF |
| 75f15fb7-c5bc-4c23-a295-163f9f5d883d | Arena:CTF Ninja Flag |
| 5a86d073-caed-46d0-88f4-a526c80e969a | Arena:Covert One Flag CTF |
| 32ed13b7-ca55-4095-bd5f-12ff91b42987 | Arena:Extraction |
| 68163569-4c13-4bc7-a59c-19f22e17d9f2 | Arena:FFA Escalation Core Slayer |
| 7c9d9ed8-2f27-4c66-8833-170ab4e80d24 | Arena:FFA King of the Hill |
| 2c9f2bcc-24ca-40e0-9a47-f5590634da64 | Arena:FFA Ninja Slayer |
| 3fcab1bb-e43c-4f7c-bf7a-eb19f0cdb7db | Arena:FFA Oddball |
| e42964e1-e19b-46f4-91cf-67802be5bef7 | Arena:FFA Shotty Snipes Slayer |
| d5305579-5310-45a8-840e-3d3beb13113f | Arena:FFA Slayer |
| d5305579-5310-45a8-840e-3d3beb13113f | Arena:FFA Slayer |
| 62deb3a5-347f-4cdf-8760-644a55bc2507 | Arena:FFA Vampire Oddball |
| 373f3d27-cb4c-4d7b-b6c9-7757de3c1133 | Arena:King of the Hill |
| 373f3d27-cb4c-4d7b-b6c9-7757de3c1133 | Arena:King of the Hill |
| 8d6e16cd-7e95-4166-92fd-d280163b7ab7 | Arena:Land Grab |
| d3aa10fe-502d-4778-8bc2-db5c3a9242ad | Arena:Oddball |

... and 85 more

---
## MatchStats - Time Distribution

| Month | Matches |
|---|---|
| 2021-11 | 365 |
| 2021-12 | 253 |
| 2022-01 | 1 |
| 2022-05 | 4 |
| 2022-06 | 98 |
| 2022-07 | 325 |
| 2022-08 | 492 |
| 2022-09 | 233 |
| 2022-10 | 111 |
| 2022-11 | 318 |
| 2022-12 | 60 |
| 2023-01 | 43 |
| 2023-02 | 143 |
| 2023-03 | 236 |
| 2023-04 | 279 |
| 2023-11 | 10 |
| 2026-04 | 216 |
| 2026-05 | 179 |

---
## OwnedInventoryItems - Sample (First 10)

| Amount | ItemId | ItemPath | ItemType | FirstAcquiredDate |
|---|---|---|---|---|
| 6 | 301-100-base-cyan-899ff22a... | Inventory/Ai/Colors/301-100-base-cyan-899ff22a.json | AiColor | 2021-11-16 12:30:10.286 |
| 6 | 301-100-base-orange-58e3a39b... | Inventory/Ai/Colors/301-100-base-orange-58e3a39b.json | AiColor | 2021-11-16 12:30:10.286 |
| 6 | 301-100-base-pink-5d69226a... | Inventory/Ai/Colors/301-100-base-pink-5d69226a.json | AiColor | 2021-11-16 12:30:10.286 |
| 1 | 301-100-base-purple-d85a184d... | Inventory/Ai/Colors/301-100-base-purple-d85a184d.json | AiColor | 2026-05-05 17:38:05.7 |
| 6 | 301-100-default-aa30213b... | Inventory/Ai/Colors/301-100-default-aa30213b.json | AiColor | 2021-11-16 12:30:10.286 |
| 1 | 301-100-default-iratu-6f24d0df... | Inventory/Ai/Colors/301-100-default-iratu-6f24d0df.json | AiColor | 2022-08-08 19:30:42.912 |
| 1 | 301-100-default-super-7e5d79f3... | Inventory/Ai/Colors/301-100-default-super-7e5d79f3.json | AiColor | 2021-12-28 20:47:43.347 |
| 1 | 301-100-epic-mixed-be-e1838a92... | Inventory/Ai/Colors/301-100-epic-mixed-be-e1838a92.json | AiColor | 2022-07-25 23:10:24.525 |
| 1 | 301-100-epic-strawber-c2c72c95... | Inventory/Ai/Colors/301-100-epic-strawber-c2c72c95.json | AiColor | 2022-08-15 14:55:19.188 |
| 1 | 301-100-epic-tangerin-e00ccb9a... | Inventory/Ai/Colors/301-100-epic-tangerin-e00ccb9a.json | AiColor | 2026-04-20 21:56:46.192 |

---
## Top 10 Playlists by Match Count

| VariantId | PublicName | Matches |
|---|---|---|
| 507191c6-a492-4331-b2ae-a172101eb23e | Ranked:CTF 5 Captures | 1449 |
| c2d20d44-8606-4669-b894-afae15b3524f | Ranked:Slayer | 1418 |
| 88c22b1f-2d64-48b9-bab1-26fe4721fb23 | Ranked:King of the Hill | 1068 |
| 751bcc9d-aace-45a1-8d71-358f0bc89f7e | Ranked:Oddball | 918 |
| 22b8a0eb-0d02-4eb3-8f56-5f63fc254f83 | Ranked:Strongholds | 842 |
| fa4dc960-5240-4aaa-8486-eb6bc0aa95aa | BRT | 504 |
| 1e8cd10b-1496-423b-8699-f98f6f5db67e | Arena:Slayer | 256 |
| 02f11d91-a43b-4205-9e55-494638949522 | Ranked:FFA Slayer | 201 |
| b0c65df9-0b2c-4040-b018-ad3e1baab832 | Ranked:Doubles Slayer | 170 |
| aca7bbf8-7a18-4aae-8785-1bd3f58275fd | Fiesta:Slayer | 72 |
