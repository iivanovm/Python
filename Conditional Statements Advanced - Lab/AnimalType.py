animals = {
    "dog": "mammal",
    "crocodile": "reptile",
    "tortoise": "reptile",
    "snake": "reptile",
}
a=input().lower()
print(animals.setdefault(a,"unknown"))