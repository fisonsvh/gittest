# 8.12
def sandwitch(*components):
    ingridients = []
    for component in components:
        print(f"Ты добавил {component} в свой сендвич")
        ingridients.append(component)
    print(f"Компонентов в твоем сендвиче – {len(ingridients)}!")
