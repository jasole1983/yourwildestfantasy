import { useSelector } from "react-redux"
import { useState, useEffect } from "react"


export default function MessageBoard() {

    const posts = useSelector(state => state.posts)

    return (
        <>
            <ul className="post_list_cont">
                {}
            </ul>



        </>
    )
}