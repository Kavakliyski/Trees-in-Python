# l = [A[C,B[D,F,E[G[H,I]]]]]

# kakwo e I?
# ako I nqma roditel        ==> e koren
# ako I nqma naslednici     ==> e listo
# ako I ima naslednici      ==> e roditel

# да се намерят всички листа (и колко са)
# да се намерят всичко родители (и колко са)
# да се намери корена на дървото (нулевата позиция)

A = [5, [1, 2, [3, 4]]]


# каква е височината на дървото или дълбочината на списъка?
# (това е и броя на родителите)?
# броя на отварящите скоби (или затварящите) е дълбочината
# броя на запетаите + 1 (заради представянето на корена) е брпя на листата
def tree_leafs(spis):
    if not spis:
        return 0
    else:
        for elem in spis:
            if not isinstance(elem, list):
                return tree_leafs(spis[1:]) + 1
            else:
                return tree_leafs(elem) + tree_leafs(spis[1:])


print("borqt na listata na durwoto e: " + str(tree_leafs(A)))


def tree_parents(spis):
    if not spis:
        return 0
    else:
        for elem in spis:
            if not isinstance(elem, list):
                return 1
        #    else:
        #       return tree_parents(elem) + tree_parents(spis[1:])


print("borqt na roditelite na durwoto e: " + str(tree_parents(A)))
