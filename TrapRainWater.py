from Logger import Logger

def calculcateArea(height, lo, hi, max_height):
    sum = 0
    for i in range(lo, hi):
        sum += max(0, max_height - height[i])
    logger.Info("  AREA BETWEEN {} AND {} FO MAX_HEIGHT {} IS {}".format(lo, hi, max_height, sum))
    return sum

def trap(height):
    logger.Info("CHECK {}".format(height))
    arr_len = len(height)
    if arr_len < 3:
        return 0
    hi = arr_len - 1
    lo = 0
    while (hi > 0) and (height[hi] < height[hi -1]):
        hi -= 1
        logger.Debug("  DECREMENTING HI TO {}".format(hi))
    while (lo < len(height) - 1) and (height[lo] < height[lo + 1]):
        lo += 1
        logger.Debug("  INCREMENTING LO TO {}".format(lo))
    lo_ptr = lo + 1
    hi_ptr = hi - 1
    area_so_far = 0
    while lo < hi:
        logger.Debug("  LO::{} HI::{} LO_PTR::{} HI_PTR::{}".format(lo,hi,lo_ptr,hi_ptr))
        if height[lo] < height[hi]:
            lo_ptr += 1
        else:
            hi_ptr -= 1

        if hi_ptr < lo_ptr:
            area_so_far += calculcateArea(height, lo + 1, hi, min(height[lo], height[hi]))
            lo = hi
        else:
            if height[lo_ptr] > height[lo]:
                if (lo_ptr - lo) > 1:
                    area_so_far += calculcateArea(height, lo + 1, lo_ptr, height[lo])
                lo = lo_ptr

            if height[hi_ptr] > height[hi]:
                if (hi - hi_ptr) > 1:
                    area_so_far += calculcateArea(height, hi_ptr + 1, hi, height[hi])
                hi = hi_ptr

    return area_so_far

if __name__ == '__main__':
    logger = Logger()
    logger.SetLogLevel(Logger.LogLevels.INFO)
    print(trap([]))
    print(trap([4,2,3]))
    print(trap([4,2,0,3,2,5]))
    print(trap([1,2,3,4,5,6]))
    print(trap([6,5,4,3,2,1]))
    print(trap([1,2,3,3,2,1]))
    print(trap([3,4,5,2,3,6,1,2,4,2,0,2,2,4,2,1,7,1,0,3,2]))
    print(trap([2,3,0,1,7,1,2,4,2,2,0,2,4,2,1,6,3,2,5,4,3]))
