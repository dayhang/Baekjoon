cx = []
cy = []
for _ in range(3):
    x, y = map(int, input().split())
    cx.append(x)
    cy.append(y)

for i in range(3):
    if cx.count(cx[i]) == 1:
        x4 = cx[i]
    if cy.count(cy[i]) == 1:
        y4 = cy[i]
print(x4, y4)