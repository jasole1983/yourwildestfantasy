import { useDispatch, useSelector } from "react-redux"
import { useState, useEffect } from "react"
import { useParams } from "react-router-dom"
import { fetchLeaguePosts } from "../../store/slices/messages"


export default function MessageBoard() {

    const { posts } = useSelector(state => state.posts)
    const { comments } = useSelector(state => state.comments)
    const { leagueId } = useParams()

    const dispatch = useDispatch()
    useEffect( () => {
        dispatch(fetchLeaguePosts())

    }, [])


    return (
        <>
            <ul className="post_list_cont">
                {posts && posts.map((post, i) => (
                    <li key={i} className={`post_list_item_${i}`}>
                        <h5>{post.title}</h5>
                            <div className="post_btn_cont">
                                <button className={`delbtn_${i}`}>X</button>
                                <button className={`edit_${i}`}>. . .</button>
                            </div>
                        <p className={`body${i}`}>{post.body}</p>
                        { comments && comments.map((comment, j) => (
                            <li key={j} className={`post_comm_list_${j}`} >
                                <div className="comm_btn_cont">
                                    <button className={`com_delbtn_${j}`}>X</button>
                                    <button className={`com_edit_${j}`}>. . .</button>
                                </div>
                                <p className={`com_body${j}`}>{comment.body}</p>
                            </li>
                        )
                        )}
                    </li>
                ))}
            </ul>



        </>
    )
}