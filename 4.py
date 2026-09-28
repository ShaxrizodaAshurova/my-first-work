ali = {"Toshkent", "Samarqand", "Buxoro", "Andijon"}
vali = {"Toshkent", "Farg'ona", "Buxoro", "Xiva"}
both_city=ali.intersection(vali)
only_ali=ali.difference(vali)
print(f"ikkalasiyam borgan shaharlar: {both_city}")
print(f"faqat ali borgan shaharlar: {only_ali}")