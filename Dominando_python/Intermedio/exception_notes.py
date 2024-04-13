try:
    print(f"Texto con formato {e}".format())
except Exception as e:
    e.add_note("Ha ocurrido un error")
    print(e.__notes__) # ['Ha ocurrido un error']