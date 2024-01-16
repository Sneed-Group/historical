#include <string>
#include <vector>

int getParent(int Instance);
std::vector<int> getChildren(int Instance);
int getChildFromName(int Instance, char* InstanceName);
int getChildFromClassName(int Instance, char* ClassName);
std::string* getInstanceName(int Instance);
std::string* getInstanceClassName(int Instance);

namespace RBX {
	class Instance
	{
	private:
		int InstanceAddress;
	public:
		Instance();
		Instance operator[](char* ChildName);
		Instance GetParent();
		std::vector<Instance> GetChildren();
		std::string* Name;
		std::string* ClassName;
		Instance FindFirstChild(char* ChildName);
		Instance FindFirstChildOfClass(char* ClassName);
		int GetAddress();
		Instance(int Address);
	};
}
