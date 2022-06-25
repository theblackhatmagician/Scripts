#include <stdio.h>
#include <dirent.h>

int main()
{
    // Path to old and new files
    char oldName[100], newName[100];
    DIR *d;
    struct dirent *dir;
    d = opendir(".");
	if (d)
    {
        while ((dir = readdir(d)) != NULL)
        {
            
            for(int i=0;i<22;i++)
            {
            	char ch[50];
            	sprintf(ch, "The.Flash.2014.S05E%d.480p.x264.mkv", i+1);
            	printf("%s",ch);
            	if (rename(dir->d_name, ch) == 0)
   				{
     				printf("File renamed successfully.\n");
     				printf("%s\n", dir->d_name);
  				}		
  			
			}
        }
        closedir(d);
    }
    return(0);

/*	for(i=0;i<22;i++)
	{
		
	}
    if (rename(oldName, newName) == 0)
    {
        printf("File renamed successfully.\n");
    }
    else
    {
        printf("Unable to rename files. Please check files exist and you have permissions to modify files.\n");
    }

    return 0;  */
}
