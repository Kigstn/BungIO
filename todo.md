# todo

- client attrs:
  - user https://bungie-net.github.io/multi/operation_get_Destiny2-GetProfile.html#operation_get_Destiny2-GetProfile
    - character https://bungie-net.github.io/multi/operation_get_Destiny2-GetCharacter.html#operation_get_Destiny2-GetCharacter
        - 👍 activities https://bungie-net.github.io/multi/operation_get_Destiny2-GetActivityHistory.html#operation_get_Destiny2-GetActivityHistory
          - 👍 pgcr https://bungie-net.github.io/multi/operation_get_Destiny2-GetPostGameCarnageReport.html#operation_get_Destiny2-GetPostGameCarnageReport
        - aggregate activity stats https://bungie-net.github.io/multi/operation_get_Destiny2-GetDestinyAggregateActivityStats.html#operation_get_Destiny2-GetDestinyAggregateActivityStats
        - whatever this is https://bungie-net.github.io/multi/operation_get_Destiny2-GetCollectibleNodeDetails.html#operation_get_Destiny2-GetCollectibleNodeDetails
        - move / lock items, etc...
        - leaderboards https://bungie-net.github.io/multi/operation_get_Destiny2-GetLeaderboardsForCharacter.html#operation_get_Destiny2-GetLeaderboardsForCharacter
        - stats https://bungie-net.github.io/multi/operation_get_Destiny2-GetHistoricalStats.html#operation_get_Destiny2-GetHistoricalStats
        - unique weapons https://bungie-net.github.io/multi/operation_get_Destiny2-GetUniqueWeaponHistory.html#operation_get_Destiny2-GetUniqueWeaponHistory
    - 👍 clan
    - item instance +info
    - vendors
    - leaderboards https://bungie-net.github.io/multi/operation_get_Destiny2-GetLeaderboards.html#operation_get_Destiny2-GetLeaderboards
    - stats https://bungie-net.github.io/multi/operation_get_Destiny2-GetHistoricalStatsForAccount.html#operation_get_Destiny2-GetHistoricalStatsForAccount
  - clan
    - leaderboards https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanLeaderboards.html#operation_get_Destiny2-GetClanLeaderboards
    - aggregate stats https://bungie-net.github.io/multi/operation_get_Destiny2-GetClanAggregateStats.html#operation_get_Destiny2-GetClanAggregateStats


# idea:
- bungio
  - client
    -> convenience methods
  - http  //done
    -> raw http which return json
  - bungie
    -> convenience methods which return python classes
  - models
    - bungie  //done
      -> all automatically generated
    - overwrites
      -> convenience methods which I wrote which overwrite the automatic ones
      -> like that a clan obj has helper methods to get members
      -> imports are from the overwrites folder, if that exists-





# build steps:
- python -m build --sdist --wheel
- twine upload dist/* -u __token__




# what do those mean
- x-dictionary-key
- x-destiny-component-type-dependency


# put all manifest models into a specific doc page
# docs for all events
# maybe @listen for events
