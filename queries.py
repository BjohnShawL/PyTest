class Queries(object):
    _get_all_users = "select firstname, lastname, created_on::VARCHAR(255),id from public.users LIMIT(100)"
    _create_new_user = "INSERT INTO public.users(firstname, lastname, created_on) VALUES (%s,%s,%s)"
    _multiLineQuery = "select firstname, lastname, created_on::VARCHAR(255) from public.users LIMIT(100);INSERT INTO public.users(firstname, lastname, created_on) VALUES (%s,%s,%s);select firstname, lastname, created_on::VARCHAR(255) from public.users LIMIT(100)"
    _delete_user = ""