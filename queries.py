class Queries(object):
    _get_all_users = "select firstname, lastname, created_on::VARCHAR(255) from public.users LIMIT(100)"
    _create_new_user = "INSERT INTO public.users(firstname, lastname, created_on) VALUES (%s,%s,%s)"