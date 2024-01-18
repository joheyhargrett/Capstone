// This is for adding items to the cart
export const addCart = (product) => {
    return {
        type: 'ADDITEM',
        payload: product
    }
}
// This is for deleting items from the cart
export const delCart = (product) => {
    return {
        type: 'DELITEM',
        payload: product
    }
}
