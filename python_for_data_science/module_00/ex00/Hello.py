#!/usr/bin/env python

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# list[] = ordered, mutable, allows duplicates, indexable
ft_list[1] = "World!"

# tuple() = ordered, immutable, allows duplicates, indexable
temp_list = list(ft_tuple)
temp_list[1] = "Germany!"
ft_tuple = tuple(temp_list)

# set{} = unordered, mutable (with add/remove), no duplicates, not indexable
ft_set.remove("tutu!")
ft_set.add("Heilbronn!")

# dict{} = insertion-ordered, mutable, keys must be unique
# (values can be duplicated), indexable by key
ft_dict["Hello"] = "42Heilbronn!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)
