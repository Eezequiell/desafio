def seg_mins(segundos):
    return segundos /60

def segs_hrs(segundos):
    return segundos / 3600

def mins_hrs(minutos):
    return minutos / 60

if __name__=="_main__":
    segundos=150
    minutos=seg_mins(segundos)
    print(f"{segundos} seg son equivalentes a {minutos} min")