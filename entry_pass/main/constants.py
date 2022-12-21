from .forms import *

FORMS_DICT = {
    'PassDayYearForm': PassDayYearForm,
    'PassNightYearForm': PassNightYearForm,
    'PassOneTimeForm': PassOneTimeForm,
    'CarForm': CarForm,
    'OwnerForm': OwnerForm
                    }

PASSES_CLASS_DICT = {'PassDayYear': PassDayYear,
                     'PassNightYear': PassNightYear,
                     'PassOneTime': PassOneTime
                     }
