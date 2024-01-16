#include "Instance.h"
#include <stdio.h>
#include <string.h>

int getParent(int Instance)
{
	return *(int*)(Instance + 0x34);
}

std::vector<int> getChildren(int Instance)
{
	std::vector<int> childrenVector;
	int childVector = *(int*)(Instance + 44);
	int childEnd = *(int*)(childVector + 4);
	int childStart = *(int*)childVector;
	int childMax = *(int*)(childVector + 4) - *(int*)(childVector) >> 3;
	int childCount = 0;
	for (; childStart != childEnd; childStart += 8)
	{
		if (childCount == childMax)
			break;
		else
		{
			childCount++;
			childrenVector.push_back(*(int*)childStart);
		}
	}
	return childrenVector;
}

int getChildFromName(int Instance, char* InstanceName)
{
	std::vector<int> childrenVector = getChildren(Instance);
	for (int child : childrenVector)
		if (!strcmp(getInstanceName(child)->c_str(), InstanceName))
			return child;
	return NULL;
}

int getChildFromClassName(int Instance, char* ClassName)
{
	std::vector<int> childrenVector = getChildren(Instance);
	for (int child : childrenVector)
		if (!strcmp(getInstanceClassName(child)->c_str(), ClassName))
			return child;
	return NULL;
}

std::string* getInstanceName(int Instance)
{
	return *(std::string**)(Instance + 0x28);
}

std::string* getInstanceClassName(int Instance)
{
	return *(std::string**)(*(int*)(Instance + 0xC) + 4);
}


RBX::Instance::Instance()
{

}

RBX::Instance RBX::Instance::operator[](char* ChildName)
{
	return this->FindFirstChild(ChildName);
}

RBX::Instance RBX::Instance::GetParent()
{
	 int Parent = getParent(this->InstanceAddress);
	 if (Parent)
		 return RBX::Instance(Parent);
	 return NULL;
}

 std::vector<RBX::Instance> RBX::Instance::GetChildren()
 {
	 std::vector<RBX::Instance> Children;
	 for (int Child : getChildren(this->InstanceAddress))
		 Children.push_back(RBX::Instance(Child));
	 return Children;
 }

 RBX::Instance RBX::Instance::FindFirstChild(char* ChildName)
 {
	 int Child = getChildFromName(this->InstanceAddress, ChildName);
	 if (Child)
		 return RBX::Instance(Child);
	 return NULL;
 }

 RBX::Instance RBX::Instance::FindFirstChildOfClass(char* ClassName)
 {
	 int Child = getChildFromClassName(this->InstanceAddress, ClassName);
	 if (Child)
		 return RBX::Instance(Child);
	 return NULL;
 }

 int RBX::Instance::GetAddress()
 {
	 return this->InstanceAddress;
 }

 RBX::Instance::Instance(int Address)
 {
	 this->InstanceAddress = Address;
	 this->Name = getInstanceName(Address);
	 this->ClassName = getInstanceClassName(Address);
 }

