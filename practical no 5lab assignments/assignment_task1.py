nums = tuple(map(int, input("Enter Tuple elements: ").split()))

print("\nTask (a) Total number of items:")
print(len(nums))

print("\nTask (b) Last item in tuple:")
print(nums[-1])

print("\nTask (c) Elements in reverse order:")
print(nums[::-1])

print("\nTask (d) Check if 5 and 0 exist:")
if 5 in nums and 0 in nums:
    print("Both 5 and 0 exist in the tuple")
else:
    print("Either 5 or 0 or both are not present")

print("\nTask (e) Tuple after removing first and last items:")
print(nums[1:-1])