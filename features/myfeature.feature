Feature: Orange Logo


Scenario: T_SPR_22 annullamentoRptMaiRichiesteDaPm
    Given the scenario precedente
    When copy
    Then check

@test
Scenario: Logo presence
    Given the T_SPR_22 annullamentoRptMaiRichiesteDaPm scenario executed successfully
     And set the stringa default
    When copy stringa
    Then check the stringa created
    And initial json checkPosition
        """
        {
            "positionslist": [
                {
                    "fiscalCode": "#creditor_institution_code#",
                    "noticeNumber": "302#iuv#"
                }
            ]
        }
        """
    
