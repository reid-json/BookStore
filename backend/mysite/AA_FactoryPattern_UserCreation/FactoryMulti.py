from AA_FactoryPattern_UserCreation.FactoryConcrete import DefaultUserFactory


def get_user_factory(user_type='default'):
    if user_type == 'default':
        return DefaultUserFactory()
    # Add more factories here