Scenario
========
Actions
-------
.. function:: db_message(database_message_id)

   Shows the predefined text of the message with ID *database_message_id*
   in the messagewidget. Displayed text is translated.

.. function:: goal_reached(goal_number)

   The player reaches the goal with ID *goal_number* in the current scenario.

.. function:: logbook(\*widgets)

   Shows a logbook entry and opens the logbook after *delay* seconds.

   
   

   Check widgets.logbook.add_captainslog_entry() for widget documentation.
   

.. function:: lose()

   The player fails the current scenario.

.. function:: message(\*messages)

   Shows a message with custom text in the messagewidget. *messages* is a list of message texts.
   If it contains more than one message, they are shown after each other, delayed in time.
   Custom messages are translated if and only if the scenario author requested translations.

.. function:: set_var(variable, value)

   Assigns the value *value* to the scenario variable *variable*.
   Overwrites the current value of *variable*.

.. function:: spawn_ships(owner_id, ship_id, number, \*position )

   
   Creates a *number* of *ship_id* type ships controlled by the player
   with world id *owner_id* around the map position *position*.




   

.. function:: wait(seconds)

   Postpones any other scenario event for *seconds* seconds.

.. function:: win()

   The player wins the current scenario. If part of a campaign, offers to start the next scenario.

Conditions
----------
.. function:: building_num_of_type_greater(building_class, limit)

   Returns whether any player settlement has more than *limit* buildings of type *building_class*.

.. function:: buildings_connected_to_building_gt(building_class, class2, limit)

   Checks whether more than *limit* of *building_class* type buildings are
   connected to any building of type *class2*.

.. function:: buildings_connected_to_building_lt(building_class, class2, limit)

   Checks whether less than *limit* of *building_class* type buildings are
   connected to any building of type *class2*.

.. function:: buildings_connected_to_warehouse_gt(building_class, limit)

   Checks whether more than *limit* of *building_class* type buildings are
   connected to a warehouse or storage.

.. function:: buildings_connected_to_warehouse_lt(building_class, limit)

   Checks whether less than *limit* of *building_class* type buildings are
   connected to a warehouse or storage.

.. function:: player_balance_greater(limit)

   Returns whether the cumulative balance of all player settlements is higher than *limit*.

.. function:: player_gold_greater(limit)

   Returns whether the player has more gold than *limit*.

.. function:: player_gold_less(limit)

   Returns whether the player has less gold than *limit*.

.. function:: player_inhabitants_greater(limit)

   Returns whether all player settlements combined have more than *limit* inhabitants.

.. function:: player_number_of_ships_gt(player_id, limit)

   Returns whether the number of ships owned by the player *player_id* is greater than *limit*.

.. function:: player_number_of_ships_lt(player_id, limit)

   Returns whether the number of ships owned by the player *player_id* is less than *limit*.

.. function:: player_produced_res_greater(resource, limit)

   Returns whether more than *limit* of the resource *resource*
   have been produced in all player settlements combined.

.. function:: player_res_stored_greater(resource, limit)

   Returns whether all player settlements combined have more than *limit*
   of *resource* in their inventories.

.. function:: player_res_stored_less(resource, limit)

   Returns whether all player settlements combined have less than *limit*
   of *resource* in their inventories.

.. function:: player_total_earnings_greater(limit)

   Returns whether the player has earned more than *limit* money with
   trading in all settlements combined. Profit = sell_income - buy_expenses.

.. function:: settlement_balance_greater(limit)

   Returns whether the balance of at least one player settlement is higher than *limit*.

.. function:: settlement_inhabitants_greater(limit)

   Returns whether at least one player settlement has more than *limit* inhabitants.

.. function:: settlement_produced_res_greater(resource, limit)

   Returns whether more than *limit* resource have been produced in any player settlement.

.. function:: settlement_res_stored_greater(resource, limit)

   Returns whether at least one player settlement has more than *limit*
   of *resource* in its inventory.

.. function:: settlements_num_greater(limit)

   Returns whether the number of player settlements is greater than *limit*.

.. function:: settler_level_greater(limit)

   Returns whether the highest increment reached in any player settlement is greater than *limit*.

.. function:: time_passed(seconds)

   Returns whether at least *seconds* seconds have passed since the game started.

.. function:: var_eq(variable, value)

   Returns whether *variable* has a value equal to *value*.
   Returns False if variable was never set in the current session.

.. function:: var_gt(variable, value)

   Returns whether *variable* has a value greater than *value*.
   Returns False if variable was never set in the current session.

.. function:: var_lt(variable, value)

   Returns whether *variable* has a value less than *value*.
   Returns False if variable was never set in the current session.

