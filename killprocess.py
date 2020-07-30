import ctypes

k_handle = ctypes.WinDLL("Kernel32.dll")


Process_All_Access = (0x000F0000 | 0x00100000 | 0xFFF)

user_in = ctypes.c_ulong(int(input("Enter processID")))

dwDesiredAccess = Process_All_Access
bInheritHandle = False
dwProcessId = user_in

response = k_handle.OpenProcess(dwDesiredAccess, bInheritHandle, dwProcessId)

if response <= 0:
    print("Handle was not obtained", k_handle.GetLastError())
else:
    print("Handle was obtained:",response)
    
uExitCode = 0x1
    
response2 = k_handle.TerminateProcess(response, uExitCode)

if response2 == 0:
    print("Could not kill process", k_handle.GetLastError())
else:
    print("Process killed")
