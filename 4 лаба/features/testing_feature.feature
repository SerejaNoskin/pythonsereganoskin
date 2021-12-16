Feature: Test
    Scenario: Test Builder
      Given Product_Builder
      When test_ATAK_builder return OK
      And test_Magnit_builder return OK
      Then Good job
