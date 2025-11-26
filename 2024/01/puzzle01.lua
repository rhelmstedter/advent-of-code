local input = [[
3   4
4   3
2   5
1   3
3   9
3   3
]]

local file = io.open("input.txt", "r")

local lhs = {}
local rhs = {}

if file then
    for line in file:lines() do
        local l, r = line:match("(%d+)%s+(%d+)")
        table.insert(lhs, tonumber(l))
        table.insert(rhs, tonumber(r))
    end
    file:close()
else
    print("Could not open file")
end

-- -- part 1
-- local diffs = 0
-- table.sort(lhs)
-- table.sort(rhs)
-- for i = 1, #lhs do
--     local l = lhs[i]
--     local r = rhs[i]
--     local diff = math.abs(tonumber(l) - tonumber(r))
--     diffs = diffs + diff
-- end
-- print(diffs)

-- part 2
local total = 0
for _, v in ipairs(lhs) do
    local l = v
    local count = 0
    for _, w in ipairs(rhs) do
        if l == w then
            count = count + 1
        end
    end
    total = total + (l * count)
end
print(total)

local inspect = require("inspect")
print(inspect(lhs))
