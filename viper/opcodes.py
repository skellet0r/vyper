opcodes = {
    'STOP': [0x00, 0, 0, 0],
    'ADD': [0x01, 2, 1, 3],
    'MUL': [0x02, 2, 1, 5],
    'SUB': [0x03, 2, 1, 3],
    'DIV': [0x04, 2, 1, 5],
    'SDIV': [0x05, 2, 1, 5],
    'MOD': [0x06, 2, 1, 5],
    'SMOD': [0x07, 2, 1, 5],
    'ADDMOD': [0x08, 3, 1, 8],
    'MULMOD': [0x09, 3, 1, 8],
    'EXP': [0x0a, 2, 1, 10],
    'SIGNEXTEND': [0x0b, 2, 1, 5],
    'LT': [0x10, 2, 1, 3],
    'GT': [0x11, 2, 1, 3],
    'SLT': [0x12, 2, 1, 3],
    'SGT': [0x13, 2, 1, 3],
    'EQ': [0x14, 2, 1, 3],
    'ISZERO': [0x15, 1, 1, 3],
    'AND': [0x16, 2, 1, 3],
    'OR': [0x17, 2, 1, 3],
    'XOR': [0x18, 2, 1, 3],
    'NOT': [0x19, 1, 1, 3],
    'BYTE': [0x1a, 2, 1, 3],
    'SHA3': [0x20, 2, 1, 30],
    'ADDRESS': [0x30, 0, 1, 2],
    'BALANCE': [0x31, 1, 1, 400],
    'ORIGIN': [0x32, 0, 1, 2],
    'CALLER': [0x33, 0, 1, 2],
    'CALLVALUE': [0x34, 0, 1, 2],
    'CALLDATALOAD': [0x35, 1, 1, 3],
    'CALLDATASIZE': [0x36, 0, 1, 2],
    'CALLDATACOPY': [0x37, 3, 0, 3],
    'CODESIZE': [0x38, 0, 1, 2],
    'CODECOPY': [0x39, 3, 0, 3],
    'GASPRICE': [0x3a, 0, 1, 2],
    'EXTCODESIZE': [0x3b, 1, 1, 700],
    'EXTCODECOPY': [0x3c, 4, 0, 700],
    'BLOCKHASH': [0x40, 1, 1, 20],
    'COINBASE': [0x41, 0, 1, 2],
    'TIMESTAMP': [0x42, 0, 1, 2],
    'NUMBER': [0x43, 0, 1, 2],
    'DIFFICULTY': [0x44, 0, 1, 2],
    'GASLIMIT': [0x45, 0, 1, 2],
    'POP': [0x50, 1, 0, 2],
    'MLOAD': [0x51, 1, 1, 3],
    'MSTORE': [0x52, 2, 0, 3],
    'MSTORE8': [0x53, 2, 0, 3],
    'SLOAD': [0x54, 1, 1, 200],
    'SSTORE': [0x55, 2, 0, 5000],
    'JUMP': [0x56, 1, 0, 8],
    'JUMPI': [0x57, 2, 0, 10],
    'PC': [0x58, 0, 1, 2],
    'MSIZE': [0x59, 0, 1, 2],
    'GAS': [0x5a, 0, 1, 2],
    'JUMPDEST': [0x5b, 0, 0, 1],
    'LOG0': [0xa0, 2, 0, 375],
    'LOG1': [0xa1, 3, 0, 750],
    'LOG2': [0xa2, 4, 0, 1125],
    'LOG3': [0xa3, 5, 0, 1500],
    'LOG4': [0xa4, 6, 0, 1875],
    'CREATE': [0xf0, 3, 1, 32000],
    'CALL': [0xf1, 7, 1, 700],
    'CALLCODE': [0xf2, 7, 1, 700],
    'RETURN': [0xf3, 2, 0, 0],
    'DELEGATECALL': [0xf4, 6, 1, 700],
    'CALLBLACKBOX': [0xf5, 7, 1, 700],
    'INVALID': [0xfe, 0, 0, 0],
    'SUICIDE': [0xff, 1, 0, 5000],
    'SELFDESTRUCT': [0xff, 1, 0, 25000],
}

pseudo_opcodes = {
    'CLAMP': [None, 3, 1, 45],
    'UCLAMPLT': [None, 2, 1, 25],
    'UCLAMPLE': [None, 2, 1, 30],
    'CLAMP_NONZERO': [None, 1, 1, 19],
    'ASSERT': [None, 1, 0, 20],
    'PASS': [None, 0, 0, 0],
    'BREAK': [None, 0, 0, 20],
    'SHA3_32': [None, 1, 1, 72],
    'SLE': [None, 2, 1, 10],
    'SGE': [None, 2, 1, 10],
    'LE': [None, 2, 1, 10],
    'GE': [None, 2, 1, 10],
    'CEIL32': [None, 1, 1, 20],
    'SET': [None, 2, 0, 20],
    'NE': [None, 2, 1, 6],
}

comb_opcodes = {}
for k in opcodes:
    comb_opcodes[k] = opcodes[k]
for k in pseudo_opcodes:
    comb_opcodes[k] = pseudo_opcodes[k]

