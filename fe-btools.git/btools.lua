--CREATED BY SPARKSAMMY
loadstring(game:HttpGet("https://raw.githubusercontent.com/sparksammy/Ownership-OpenGamer/main/ownership.lua"))()
local Tool = Instance.new("Tool",game.Players.LocalPlayer.Backpack)
local Equipped = false

Tool.RequiresHandle = false
Tool.Name = "Delete Tool"
Tool.ToolTip = "Made by Sparksammy."
local Field = Instance.new("SelectionBox",game.Workspace)
local Mouse = game.Players.LocalPlayer:GetMouse()
Field.LineThickness = 0.1

Tool.Equipped:connect(function()
Equipped = true

while Equipped == true do
if Mouse.Target ~= nil then
Field.Adornee = Mouse.Target

else
Field.Adornee = nil
end
wait()
end
end)


Tool.Unequipped:connect(function()
Equipped = false
Field.Adornee = nil
end)

Tool.Activated:connect(function()
if Mouse.Target ~= nil then
local targetPart = Mouse.Target
local forceArg = Vector3.new(-9000000000, -9000000000, -9000000000)
local thrust = Instance.new("BodyThrust")
targetPart.Anchored = false
thrust.Parent = targetPart
thrust.Force = forceArg
thrust.Location = targetPart.Position
targetPart.CFrame = targetPart.CFrame - Vetor3.new(25,25,25)
local ex = Instance.new('Explosion')
ex.BlastRadius = 0
ex.Position = Mouse.Target.Position
ex.Parent = workspace
local AttemptTarget = Mouse.Target
while AttemptTarget ~= nil do
AttemptTarget.Velocity = forceArg
AttemptTarget.CanCollide = false
wait(2)
end

end
end)
