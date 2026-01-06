# Complete the new_resizer function using currying. It should make sure the image dimensions are never smaller than the minimum width and height, or larger than the maximum width and height specified.

# Check the example at the bottom to see how it is intended to be called.

# In the new_resizer body, define an inner function that takes two optional integer inputs min_width and min_height with default values of 0, and in its body:
# If min_width is more than max_width or min_height is more than max_height, raise an exception "minimum size cannot exceed maximum size".
# Define an innermost function that takes two integer inputs width and height, and in its body:
# Use the built-in min and max functions to reduce width if it's above max_width or increase it if it's below min_width.
# Do the same for height.
# Return the new width and height.
# Return the innermost function.
# Return the inner function.


# # Step 1: Create the resizer with maximum dimensions
# set_min_size = new_resizer(800, 600)

# # Step 2: Set the minimum dimensions
# resize_image = set_min_size(200, 100)

# # Step 3: Resize the image
# new_width, new_height = resize_image(1000, 500)

# # Step 4: Output the result
# print(new_width, new_height)  # Output: 800, 500

# # With currying syntax
# print(new_resizer(800, 600)(200, 100)(1000, 500))  # Output: (800, 500)



def new_resizer(max_width, max_height):
    def set_min_size(min_w = 0, min_h=0):
        if min_w > max_width or min_h > max_height:
            raise Exception('minimum size cannot exceed maximum size')
        def resize_image(width, height):
            computed_h = min(max(height, min_h),max_height)
            computed_w = min(max(width, min_w),max_width)            
            return computed_w, computed_h
        return resize_image
    return set_min_size
            