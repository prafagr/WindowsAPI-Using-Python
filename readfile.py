import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll")

lpFileName = "C:\\Users\\test_sym\\Desktop\\file.txt"
dwDesiredAccess = 0x10000000
dwShareMode = 0x0
lpSecurityAttributes = None
dwCreationDisposition = 0x3
dwFlagsAndAttributes = 0x80
hTemplateFile = None

response = k_handle.CreateFileW(lpFileName, dwDesiredAccess, dwShareMode, lpSecurityAttributes, dwCreationDisposition, dwFlagsAndAttributes, hTemplateFile)
print("Value of response", response)
if response == -1:
    print("Error", k_handle.GetLastError())
else:
    print("Handle obtained")
    
hFile = response
lpBuffer = ctypes.create_string_buffer(100)
#lpBuffer = ctypes.c_wchar_p()
nNumberOfBytesToRead = 0x10000
lpNumberOfBytesRead = ctypes.c_ulong()
lpOverlapped = None

response2 = k_handle.ReadFile(hFile, ctypes.byref(lpBuffer), nNumberOfBytesToRead, ctypes.byref(lpNumberOfBytesRead),lpOverlapped)
print("Number of bytes read",lpNumberOfBytesRead.value)

count = lpNumberOfBytesRead
if response2 == 0:
    print("Error",k_handle.GetLastError())
else:
    print("File read", lpBuffer.value)
