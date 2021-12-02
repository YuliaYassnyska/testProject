class Locators():

    #main page locators
    searchBoxFrom = '//*[@id="from"]'
    chooseFrom = '//span[text()="Львів"]'
    searchBoxTo = '//*[@id="to"]'
    chooseTo = '//span[text()="Київ"]'
    calendar = '//div[@class="Styled__FormWrapper-sc-1wmj83m-4 iSLDVz"]'
    nextMonth = '//div[@class="Styled__DaypickerIconNavigation-sc-1vjhvhi-6 lnfeLk"]'
    day = '//span[text()="9"]'
    buttonFind = '//button[@class="Styled__ResettedButton-sc-1dxewfu-0 Styled__ColoredButton-sc-1dxewfu-1 Styled__SizedButton-sc-1dxewfu-2 Styled__StyledButton-sc-1dxewfu-3 erLGFn Style__Submit-sc-1ppxt07-3 ljhOaC"]'
    findTicket = '//span[text()="Euroclub"]'
    buttonFindTicket = '//div[@class="ticket"][5]/div/div[2]/div/div[3]/div/div[2]/button'

    #flight selection locator
    continueButt = '//button[@class="Styled__ResettedButton-sc-1dxewfu-0 Styled__ColoredButton-sc-1dxewfu-1 Styled__SizedButton-sc-1dxewfu-2 Styled__StyledButton-sc-1dxewfu-3 dVhHli preorder__submit preorder__submit--fixed"]'

    #passengers locators
    firstName = '//input[@id="checkout_passenger1_1021051141151169511097109101"]'
    lastName = '//input[@id="checkout_passenger1_108971151169511097109101"]'
    scrollToInfo = '//span[@class="verify-panel__picker-description"]'
    email = '//input[@id="checkout_email"]'
    number = '//input[@id="checkout_phone"]'
    scrollToPay = '//div[@class="checkout__payment-header"]'
    checkConditions = '//div[@class="checkout__agreement checkout__custom-checkbox flat__form"]/div/div/label'
    nextCheck = '//div[@class="m-verify-panel__policy"]/div/label'
    buttGoToPay = '//div[@class="checkout-submit-btn"]'

    #locators for assert
    assCalendar = '//input[@id="on"]'
    assTickets = '//div[@class="ticket"]'