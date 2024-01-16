--[[
	 No FE GUI by Sparksammy
	 Made With Gui to Lua Converter because it's easier.
--]]



-- Instances:

local NoFE_GUI = Instance.new("ScreenGui")
local Frame = Instance.new("Frame")
local src = Instance.new("TextBox")
local exec = Instance.new("TextButton")
local mini = Instance.new("TextButton")

--[[
	Properties:
--]]

NoFE_GUI.Name = "NoFE_GUI"
NoFE_GUI.Parent = game.Players.LocalPlayer:WaitForChild("PlayerGui")
NoFE_GUI.ZIndexBehavior = Enum.ZIndexBehavior.Sibling

Frame.Parent = NoFE_GUI
Frame.BackgroundColor3 = Color3.new(1, 1, 1)
Frame.Position = UDim2.new(0.0354609936, 0, 0.494983286, 0)
Frame.Size = UDim2.new(0, 493, 0, 209)

src.Name = "src"
src.Parent = Frame
src.BackgroundColor3 = Color3.new(1, 1, 1)
src.Position = UDim2.new(-0.00105014816, 0, -0.0009521842, 0)
src.Size = UDim2.new(1, 0, 0.889999986, 0)
src.Font = Enum.Font.SourceSans
src.PlaceholderText = "Enter your script here, and it'll be executed like ROBLOX pre-FE!"
src.Text = ""
src.TextColor3 = Color3.new(0, 0, 0)
src.TextScaled = true
src.TextSize = 14
src.TextWrapped = true

exec.Name = "exec"
exec.Parent = Frame
exec.BackgroundColor3 = Color3.new(0, 1, 0)
exec.BorderColor3 = Color3.new(0, 0.333333, 0)
exec.Position = UDim2.new(-0.00105016306, 0, 0.896465063, 0)
exec.Size = UDim2.new(1, 0, 0.100000001, 0)
exec.Font = Enum.Font.SourceSans
exec.Text = "EXECUTE"
exec.TextColor3 = Color3.new(0, 0, 0)
exec.TextScaled = true
exec.TextSize = 14
exec.TextWrapped = true

mini.Name = "mini"
mini.Parent = NoFE_GUI
mini.BackgroundColor3 = Color3.new(0.415686, 1, 0.913726)
mini.Position = UDim2.new(0.0344478488, 0, 0.46488294, 0)
mini.Size = UDim2.new(0.0500000007, 0, 0.0500000007, 0)
mini.Font = Enum.Font.SourceSans
mini.Text = "-"
mini.TextColor3 = Color3.new(0, 0, 0)
mini.TextScaled = true
mini.TextSize = 14
mini.TextWrapped = true
function minimize()
	if Frame.Visible == true then
		Frame.Visible = false
	elseif Frame.Visible == false then
		Frame.Visible = true
	end
end

mini.MouseButton1Click:Connect(minimize)

function execute()
	game.ReplicatedStorage.NoFELoadString:FireServer(src.Text)
end
exec.MouseButton1Click:Connect(execute)