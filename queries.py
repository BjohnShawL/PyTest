class Queries(object):
    _get_all_users = "select firstname, lastname, created_on::VARCHAR(255),id from public.users LIMIT(100)"
    _get_single_user = "Select firstname, lastname, created_on::VARCHAR(255),id from public.users WHERE firstname LIKE %s"
    _create_new_user = "INSERT INTO public.users(firstname, lastname, created_on) VALUES (%s,%s,%s)"
    _multiLineQuery = "select firstname, lastname, created_on::VARCHAR(255) from public.users LIMIT(100);INSERT INTO public.users(firstname, lastname, created_on) VALUES (%s,%s,%s);select firstname, lastname, created_on::VARCHAR(255) from public.users LIMIT(100)"
    _delete_user = "DELETE FROM public.users where id = %s"

    _get_all_ship_classes = "select id, name, fuel_capacity, crew_size, passenger_capacity FROM public.ship_class LIMIT(100)"
    _create_new_ship_class = "INSERT INTO public.ship_class(name, fuel_capacity, crew_size, passenger_capacity) VALUES(%s,%s,%s,%s)"