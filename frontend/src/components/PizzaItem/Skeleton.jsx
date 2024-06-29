import React from "react"
import ContentLoader from "react-content-loader"

const Skeleton = (props) => (
    <ContentLoader
        className="pizza-block"
        speed={2}
        width={279}
        height={466}
        viewBox="0 0 279 466"
        backgroundColor="#f3f3f3"
        foregroundColor="#ecebeb"
        {...props}
    >
        <circle cx="130" cy="114" r="114" />
        <rect x="5" y="285" rx="22" ry="22" width="270" height="87" />
        <rect x="3" y="386" rx="20" ry="20" width="101" height="39" />
        <rect x="135" y="382" rx="26" ry="26" width="141" height="49" />
        <rect x="5" y="242" rx="15" ry="15" width="269" height="30" />
    </ContentLoader>
)

export default Skeleton
