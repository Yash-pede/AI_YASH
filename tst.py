query = str({
    "text": "तू पागल है"
})
star = query.find(":")
en = query.find("\'", 7+3)
print(query[(star+3):en])
