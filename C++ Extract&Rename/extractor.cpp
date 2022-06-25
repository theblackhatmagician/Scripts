int main()
{
    vector<wstring> files;

    if (ListFiles(L"folder", L"*", files))
    {
        string program = "\"C:\\Program Files\\WinRAR\\winrar.exe\"";
        string args = "x -y";
        string type = "*.*";

        TCHAR dir[MAX_PATH];
        GetCurrentDirectory(MAX_PATH, dir);
        wstring current_directory(wstring(L"\"") + dir + wstring(L"\\"));

        for (const auto& f : files)
        {
            if (wcscmp(PathFindExtension(f.c_str()), L".rar") == 0 ||
                wcscmp(PathFindExtension(f.c_str()), L".zip") == 0)
            {
                string file = ws2s(f.c_str());
                string output = "\"c:\\Users\\my name\\Desktop\\output\"";

                string command = program + " " + args + " " + ws2s(current_directory) + file + "\"" + " " + type + " " + output;
                cout << command << endl;

                if (system(command.c_str()) != 0)
                    return GetLastError();
            }
        }
    }

    return 0;
}
