# Write your code here
"""function removeDuplicates(xs)
{
    const result = [];

    for ( const x of xs )
    {
        // result.includes(x) is slow
        // In order to speed it up, you will need to keep
        // a separate set that contains the same elements as the list result
        // Because it is a set, the includes operation will go much faster
        if ( !result.includes(x) )
        {
            result.push(x);
        }
    }

    return result;
}"""

def remove_duplicates(xs):
    qs = set()
    result = []
    for i in xs:
        if i not in qs:
            result.append(i)
            qs.add(i)
    return result
"""  
def remove_duplicates(xs):
    found = set()
    result = []
    for x in xs:
        if x not in found:
            result.append(x)
            found.add(x)
    return result


def remove_duplicates_using_list(xs):
    found = []
    result = []
    for x in xs:
        if x not in found:
            result.append(x)
            found.append(x)
    return result
"""