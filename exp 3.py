def gs():
    be=float(input("enter salary(be):"))
    ds=be*0.70
    tr=be*0.30
    hr=be*0.10
    gross_salary=be+ds+tr+hr
    print(f"Gross salary={gross_salary}")

gs()