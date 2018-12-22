import re
allProperties = (dir(str()))

public = [val for val in allProperties if not val.startswith('_')]
private = [val for val in allProperties if val.startswith('_')]

for val in public:
    print(val)
for val in private:
    print(val)