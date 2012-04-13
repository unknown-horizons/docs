Scenario
========
Actions
-------
.. function:: logbook_w(widgets)

   Adds an entry to the logbook and displays it.

.. function:: win()

   Called when player won

.. function:: db_message(message_id)

   Shows a message specified in the db on the ingame message widget

.. function:: spawn_ships(owner, id, number, *position )

   
   spawns a number of ships for owner




   

.. function:: set_var(name, value)



.. function:: goal_reached(goal_number)

   Called when player reached a goal in a scenario

.. function:: lose()

   Called when player lost

.. function:: message(, *message )

   Shows a custom message in the messagewidget. If you pass more than one message, they
   will be shown after each other after a delay

.. function:: logbook(, *widgets )

   Show a logbook entry delayed by delay seconds.

   Set delay=0 for instant appearing.
   
   

.. function:: wait(time)



Conditions
----------
.. function:: player_gold_less(limit)

   Returns whether the player has less gold then limit

.. function:: settlements_num_greater(limit)

   Returns whether the number of settlements owned by the human player is greater than limit.

.. function:: player_inhabitants_greater(limit)

   Returns whether all settlements of player combined have more than limit inhabitants

.. function:: buildings_connected_to_building_lt(building_class, class2, number)

   Checks whether less than number of building_class type buildings are
   connected to any building of type class2.

.. function:: settlement_balance_greater(limit)

   Returns whether at least one settlement of player has a balance > limit

.. function:: player_gold_greater(limit)

   Returns whether the player has more gold then limit

.. function:: time_passed(secs)

   Returns whether at least secs seconds have passed since start.

.. function:: settlement_inhabitants_greater(limit)

   Returns whether at least one settlement of player has more than limit inhabitants

.. function:: building_num_of_type_greater(building_class, limit)

   Check if player has more than limit buildings on a settlement

.. function:: settler_level_greater(limit)

   Returns wheter the max level of settlers is greater than limit

.. function:: buildings_connected_to_warehouse_gt(building_class, number)

   Checks whether more than number of building_class type buildings are
   connected to a warehouse or storage.

.. function:: player_balance_greater(limit)

   Returns whether the cumulative balance of all player settlements is > limit

.. function:: settlement_res_stored_greater(res, limit)

   Returs whether at least one settlement of player has more than limit of res

.. function:: var_lt(name, value)

   Variable less than...

.. function:: _building_connected_to_all_of(building_class, *classes )

   Returns the exact amount of buildings of type building_class that are
   connected to any building of each class in classes. Counts all settlements.

.. function:: buildings_connected_to_building_gt(building_class, class2, number)

   Checks whether more than number of building_class type buildings are
   connected to any building of type class2.

.. function:: player_res_stored_less(res, limit)

   Returns whether all settlements of player combined have less than limit of res

.. function:: settlement_produced_res_greater(res, limit)

   Returns whether more than limit res have been produced at one of the player's settlements

.. function:: buildings_connected_to_warehouse_lt(building_class, number)

   Checks whether less than number of building_class type buildings are
   connected to a warehouse or storage.

.. function:: player_res_stored_greater(res, limit)

   Returns whether all settlements of player combined have more than limit of res

.. function:: player_number_of_ships_gt(player_id, number)



.. function:: _building_connected_to_any_of(building_class, *classes )

   Returns the exact amount of buildings of type building_class that are
   connected to any building of a class in classes. Counts all settlements.

.. function:: player_number_of_ships_lt(player_id, number)



.. function:: player_total_earnings_greater(total)

   Returns whether the player has earned more then 'total' money with trading
   earning = sell_income - buy_expenses

.. function:: player_produced_res_greater(res, limit)

   Returns whether more than limit res have been produced at all of the player's settlements combined

.. function:: var_gt(name, value)

   Variable greater than...

.. function:: var_eq(name, value)



