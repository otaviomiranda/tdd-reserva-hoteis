from src.hotel_chain import HotelChain
from src.customer import Customer
from datetime import datetime


def prepare_entry(entry: str) -> str and list:
    entry = entry.replace(" ", "")
    entry = entry.split(":")
    dates_str = entry[1].split(",")

    dates = []
    for date_str in dates_str:
        date = datetime.strptime(date_str[:9], "%d%b%Y")
        dates.append(date)

    return entry[0], dates

def main(entry: str) -> None:
    hotel_chain = HotelChain()

    hotel_chain.add_hotel("Parque das flores", 3, 110, 80, 90, 80)
    hotel_chain.add_hotel("Jardim Botânico", 4, 160, 110, 60, 50)
    hotel_chain.add_hotel("Mar Atlântico", 5, 220, 100, 150, 40)

    # customer_type, dates = prepare_entry("Fidelidade: 26Mar2020(thur), 27Mar2020(fri), 28Mar2020(sat)")
    customer_type, dates = prepare_entry(entry)
    customer = Customer(customer_type)
    
    cheaper_hotel_name = hotel_chain.get_cheaper_hotel(customer, dates)
    print(cheaper_hotel_name)
    return cheaper_hotel_name


if __name__ == "__main__":

    main()

    # hotel_chain = HotelChain()

    # hotel_chain.add_hotel("Parque das flores", 3, 110, 80, 90, 80)
    # hotel_chain.add_hotel("Jardim Botânico", 4, 160, 110, 60, 50)
    # hotel_chain.add_hotel("Mar Atlântico", 5, 220, 100, 150, 40)

    # customer_type, dates = prepare_entry("Fidelidade: 26Mar2020(thur), 27Mar2020(fri), 28Mar2020(sat)")
    # customer = Customer(customer_type)
    
    # print(hotel_chain.get_cheaper_hotel(customer, dates))