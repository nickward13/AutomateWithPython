theBoard = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
inventory = {'gold coin': 42, 'rope': 1, 'torch': 6, 'dagger': 1, 'arrow': 12}

def isValidChessBoard(board):
    
    # Check if the board is a dictionary
    if type(board) != dict:
        return False
    
    # Check if the board has no more than 32 pieces
    if len(board) > 32:
        return False
    
    # Check if board has only one black king and one white king
    blackKing = 0
    whiteKing = 0
    for k, v in board.items():
        if v == 'bking':
            blackKing += 1
        elif v == 'wking':
            whiteKing += 1
    if blackKing != 1 or whiteKing != 1:
        return False
    
    # Check if each player has at most 16 pieces
    blackPieces = 0
    whitePieces = 0
    for k, v in board.items():
        if v[0] == 'b':
            blackPieces += 1
        elif v[0] == 'w':
            whitePieces += 1
    if blackPieces > 16 or whitePieces > 16:
        return False
    
    # Check if each piece is on a valid space
    for k, v in board.items():
        if int(k[0]) not in range(1, 8) or k[1] not in "abcdefgh":
            return False
        if v[0] not in "bw":
            return False
        if v[1:] not in "pawn rook knight bishop queen king".split():
            return False

    return True

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total += v
    print("Total number of items: " + str(item_total))

def addToInventory(inventory, addedItems):
    for item in addedItems:
        inventory.setdefault(item, 0)
        inventory[item] += 1
    return inventory

print("Is the board valid? " + str(isValidChessBoard(theBoard)))

displayInventory(inventory)

inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)