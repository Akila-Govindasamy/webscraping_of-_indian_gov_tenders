
def generate_metadata():
        metadata = '''
        Author: Akila Govindasamy
        Date Of Creation: 18th September 2023
        Contents: Details of Various Tenders issued by Organizations under Government of India
        Data Source: https://etenders.gov.in/eprocure/app
        Method of Data Generation: Web-Crawling
        Tools Used: Python Selenium Library and Beautifulsoup4

        Fields:
            Organisation Chain 
            Tender Reference Number 
            Tender ID 
            Withdrawal Allowed
            Tender Type 
            Form Of Contract 
            Tender Category 
            No. of Covers
            General Technical Evaluation Allowed 
            ItemWise Technical Evaluation Allowed
            Payment Mode 
            Is Multi Currency Allowed For BOQ 
            Is Multi Currency Allowed For Fee
            Allow Two Stage Bidding 
            Tender Fee in ₹ 
            Fee Payable To 
            Fee Payable At
            Tender Fee Exemption Allowed 
            EMD Amount in ₹ 
            EMD through BG/ST or EMD Exemption Allowed
            EMD Fee Type 
            EMD Percentage 
            EMD Payable To 
            EMD Payable At 
            Title 
            Work Description
             NDA/Pre Qualification 
            Independent External Monitor/Remarks 
            Tender Value in ₹
            Product Category 
            Sub category 
            Contract Type 
            Bid Validity(Days) 
            Period Of Work(Days)          
            Location 
            Pincode 
            Pre Bid Meeting Place 
            Pre Bid Meeting Address 
            Pre Bid Meeting Date
            Bid Opening Place 
            Should Allow NDA Tender 
            Allow Preferential Bidder 
            Published Date
            Bid Opening Date 
            Document Download / Sale Start Date 
            Document Download / Sale End Date
            Clarification Start Date 
            Clarification End Date 
            Bid Submission Start Date
            Bid Submission End Date 
            Name 
            Address
        '''
        file = open('./metadata.txt', 'w', encoding='utf-8')
        file.writelines(metadata)
        file.close()
        return
