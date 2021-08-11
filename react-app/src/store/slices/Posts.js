import React, { useEffect } from 'react'
import { useDispatch, useSelector } from 'react-redux'
import { getPosts, selectPosts } from './Postslice'
import { Panel, PanelGroup, IconButton } from 'rsuite'
import { selectComments, getComments } from './CommentSlice'

export const Posts = () => {
    const dispatch = useDispatch()
    const comments = useSelector(selectComments)
    const posts = useSelector(selectPosts)


    useEffect(() => {
        dispatch(getPosts())
        dispatch(getComments())
    }, [dispatch])

    return (
        <>
            <PanelGroup>
                {posts.map( (post, i) => {
                    const currentPostComments = comments.filter((comment) => comment.postId === post.id)
                    if (currentPostComments.length > 0){
                        return (
                            <PanelGroup key={i}>
                                <Panel key={i} shaded={true} bordered={true} collapsible={true} header={post.title} >
                                    {post.body}
                                    <IconButton color='cyan' size='md' icon={<icon icon={'reply'} />} appearance='primary' onClick='' placement='left' >Reply</IconButton>
                                    <IconButton color='red' size='md' circle={true} icon={<icon icon={'close'} /> } onClick='' />
                                    <IconButton appearance='ghost' size='md' icon={<icon icon={'edit'} />} onClick=''/>
                                </Panel>
                                {currentPostComments.map( (comment, j) => {
                                    return (
                                        <Panel key={j} shaded={true} bordered={true} collapsible={true} >
                                            {comment.body}
                                            <IconButton color='cyan' size='md' icon={<icon icon={'reply'} />} appearance='primary' onClick='' placement='left' >Reply</IconButton>
                                            <IconButton color='red' size='md' circle={true} icon={<icon icon={'close'} /> } onClick='' />
                                            <IconButton appearance='ghost' size='md' icon={<icon icon={'edit'} />} onClick=''/>
                                            </Panel>
                                    )
                                })}
                            </PanelGroup>
                        )} else {
                            return (
                                <Panel key={i} shaded={true} bordered={true} collapsible={true} header={post.title}>
                                    {post.body}
                                    <IconButton color='cyan' size='md' icon={<icon icon={'reply'} />} appearance='primary' onClick='' placement='left' >Reply</IconButton>
                                    <IconButton color='red' size='md' circle={true} icon={<icon icon={'close'} /> } onClick='' />
                                    <IconButton appearance='ghost' size='md' icon={<icon icon={'edit'} />} onClick=''/>
                                </Panel>
                                )

                            }})}
                </PanelGroup>

        </>
        
    )
}
