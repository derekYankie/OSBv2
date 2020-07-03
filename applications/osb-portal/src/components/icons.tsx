import * as React from "react";
import SvgIcon, { SvgIconProps } from "@material-ui/core/SvgIcon";
import Icon from "@material-ui/core/Icon";
export {
  Close as CloseIcon,
  Add as AddIcon,
  Share as ShareIcon,
  Link as FileLinkIcon,
} from "@material-ui/icons";

export const CircleIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 15 15" {...props}>
    <path d="M7.5 0C3.35685 0 0 3.35685 0 7.5C0 11.6431 3.35685 15 7.5 15C11.6431 15 15 11.6431 15 7.5C15 3.35685 11.6431 0 7.5 0ZM7.5 13.5484C4.15827 13.5484 1.45161 10.8417 1.45161 7.5C1.45161 4.15827 4.15827 1.45161 7.5 1.45161C10.8417 1.45161 13.5484 4.15827 13.5484 7.5C13.5484 10.8417 10.8417 13.5484 7.5 13.5484Z" />
  </SvgIcon>
);

export const SquareCirclesIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 15 15" {...props}>
    <path d="M2.10938 4.21875C0.946312 4.21875 0 3.27244 0 2.10938C0 0.946312 0.946312 0 2.10938 0C3.27244 0 4.21875 0.946312 4.21875 2.10938C4.21875 3.27244 3.27244 4.21875 2.10938 4.21875ZM2.10938 1.17188C1.59245 1.17188 1.17188 1.59245 1.17188 2.10938C1.17188 2.6263 1.59245 3.04688 2.10938 3.04688C2.6263 3.04688 3.04688 2.6263 3.04688 2.10938C3.04688 1.59245 2.6263 1.17188 2.10938 1.17188ZM2.10938 15C0.946312 15 0 14.0537 0 12.8906C0 11.7276 0.946312 10.7812 2.10938 10.7812C3.27244 10.7812 4.21875 11.7276 4.21875 12.8906C4.21875 14.0537 3.27244 15 2.10938 15ZM2.10938 11.9531C1.59245 11.9531 1.17188 12.3737 1.17188 12.8906C1.17188 13.4076 1.59245 13.8281 2.10938 13.8281C2.6263 13.8281 3.04688 13.4076 3.04688 12.8906C3.04688 12.3737 2.6263 11.9531 2.10938 11.9531ZM2.10938 9.60938C0.946312 9.60938 0 8.66306 0 7.5C0 6.33694 0.946312 5.39062 2.10938 5.39062C3.27244 5.39062 4.21875 6.33694 4.21875 7.5C4.21875 8.66306 3.27244 9.60938 2.10938 9.60938ZM2.10938 6.5625C1.59245 6.5625 1.17188 6.98307 1.17188 7.5C1.17188 8.01693 1.59245 8.4375 2.10938 8.4375C2.6263 8.4375 3.04688 8.01693 3.04688 7.5C3.04688 6.98307 2.6263 6.5625 2.10938 6.5625ZM12.8906 4.21875C11.7276 4.21875 10.7812 3.27244 10.7812 2.10938C10.7812 0.946312 11.7276 0 12.8906 0C14.0537 0 15 0.946312 15 2.10938C15 3.27244 14.0537 4.21875 12.8906 4.21875ZM12.8906 1.17188C12.3737 1.17188 11.9531 1.59245 11.9531 2.10938C11.9531 2.6263 12.3737 3.04688 12.8906 3.04688C13.4076 3.04688 13.8281 2.6263 13.8281 2.10938C13.8281 1.59245 13.4076 1.17188 12.8906 1.17188ZM12.8906 15C11.7276 15 10.7812 14.0537 10.7812 12.8906C10.7812 11.7276 11.7276 10.7812 12.8906 10.7812C14.0537 10.7812 15 11.7276 15 12.8906C15 14.0537 14.0537 15 12.8906 15ZM12.8906 11.9531C12.3737 11.9531 11.9531 12.3737 11.9531 12.8906C11.9531 13.4076 12.3737 13.8281 12.8906 13.8281C13.4076 13.8281 13.8281 13.4076 13.8281 12.8906C13.8281 12.3737 13.4076 11.9531 12.8906 11.9531ZM12.8906 9.60938C11.7276 9.60938 10.7812 8.66306 10.7812 7.5C10.7812 6.33694 11.7276 5.39062 12.8906 5.39062C14.0537 5.39062 15 6.33694 15 7.5C15 8.66306 14.0537 9.60938 12.8906 9.60938ZM12.8906 6.5625C12.3737 6.5625 11.9531 6.98307 11.9531 7.5C11.9531 8.01693 12.3737 8.4375 12.8906 8.4375C13.4076 8.4375 13.8281 8.01693 13.8281 7.5C13.8281 6.98307 13.4076 6.5625 12.8906 6.5625ZM7.5 4.21875C6.33694 4.21875 5.39062 3.27244 5.39062 2.10938C5.39062 0.946312 6.33694 0 7.5 0C8.66306 0 9.60938 0.946312 9.60938 2.10938C9.60938 3.27244 8.66306 4.21875 7.5 4.21875ZM7.5 1.17188C6.98307 1.17188 6.5625 1.59245 6.5625 2.10938C6.5625 2.6263 6.98307 3.04688 7.5 3.04688C8.01693 3.04688 8.4375 2.6263 8.4375 2.10938C8.4375 1.59245 8.01693 1.17188 7.5 1.17188ZM7.5 15C6.33694 15 5.39062 14.0537 5.39062 12.8906C5.39062 11.7276 6.33694 10.7812 7.5 10.7812C8.66306 10.7812 9.60938 11.7276 9.60938 12.8906C9.60938 14.0537 8.66306 15 7.5 15ZM7.5 11.9531C6.98307 11.9531 6.5625 12.3737 6.5625 12.8906C6.5625 13.4076 6.98307 13.8281 7.5 13.8281C8.01693 13.8281 8.4375 13.4076 8.4375 12.8906C8.4375 12.3737 8.01693 11.9531 7.5 11.9531ZM7.5 9.60938C6.33694 9.60938 5.39062 8.66306 5.39062 7.5C5.39062 6.33694 6.33694 5.39062 7.5 5.39062C8.66306 5.39062 9.60938 6.33694 9.60938 7.5C9.60938 8.66306 8.66306 9.60938 7.5 9.60938ZM7.5 6.5625C6.98307 6.5625 6.5625 6.98307 6.5625 7.5C6.5625 8.01693 6.98307 8.4375 7.5 8.4375C8.01693 8.4375 8.4375 8.01693 8.4375 7.5C8.4375 6.98307 8.01693 6.5625 7.5 6.5625Z" />
  </SvgIcon>
);

export const ChartIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 18 18" {...props}>
    <path d="M17.5781 15.75C17.8102 15.75 18 16.0031 18 16.3125V17.4375C18 17.7469 17.8102 18 17.5781 18H0.421875C0.189844 18 0 17.7469 0 17.4375V0.5625C0 0.253125 0.189844 0 0.421875 0H1.26562C1.49766 0 1.6875 0.253125 1.6875 0.5625V15.75H17.5781ZM5.0625 12.9375V9.5625C5.0625 9.25313 4.87266 9 4.64062 9H3.79688C3.56484 9 3.375 9.25313 3.375 9.5625V12.9375C3.375 13.2469 3.56484 13.5 3.79688 13.5H4.64062C4.87266 13.5 5.0625 13.2469 5.0625 12.9375ZM8.4375 12.9375V3.5625C8.4375 3.25312 8.24766 3 8.01562 3H7.17188C6.93984 3 6.75 3.25312 6.75 3.5625V12.9375C6.75 13.2469 6.93984 13.5 7.17188 13.5H8.01562C8.24766 13.5 8.4375 13.2469 8.4375 12.9375ZM11.8125 12.9375V6.5625C11.8125 6.25313 11.6227 6 11.3906 6H10.5469C10.3148 6 10.125 6.25313 10.125 6.5625V12.9375C10.125 13.2469 10.3148 13.5 10.5469 13.5H11.3906C11.6227 13.5 11.8125 13.2469 11.8125 12.9375ZM15.1875 12.9375V2.0625C15.1875 1.75312 14.9977 1.5 14.7656 1.5H13.9219C13.6898 1.5 13.5 1.75312 13.5 2.0625V12.9375C13.5 13.2469 13.6898 13.5 13.9219 13.5H14.7656C14.9977 13.5 15.1875 13.2469 15.1875 12.9375Z" />
  </SvgIcon>
);

export const CubeIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 15 15" {...props}>
    <path d="M14.7154 4.67882L7.8599 0.108491C7.6259 -0.0355037 7.37618 -0.0368221 7.14005 0.108491L0.284589 4.67882C0.108808 4.79598 0 5.00527 0 5.21451V9.78481C0 9.99408 0.108808 10.2033 0.284619 10.3205L7.14007 14.8915C7.37407 15.0355 7.62379 15.0368 7.85993 14.8915L14.7154 10.3205C14.8912 10.2034 15 9.99408 15 9.78481V5.21451C15 5.00527 14.8912 4.79598 14.7154 4.67882ZM8.14452 1.84952L13.1919 5.21451L10.9403 6.72123L8.14452 4.85457V1.84952ZM6.85546 1.84952V4.85457L4.05969 6.72123L1.80802 5.21451L6.85546 1.84952ZM1.28906 6.41988L2.90457 7.49968L1.28906 8.57948V6.41988ZM6.85546 13.1498L1.80802 9.78484L4.05969 8.27813L6.85546 10.1448V13.1498ZM7.49999 9.02312L5.22318 7.49968L7.49999 5.97624L9.77679 7.49968L7.49999 9.02312ZM8.14452 13.1498V10.1448L10.9403 8.27813L13.1919 9.78484L8.14452 13.1498ZM13.7109 8.57948L12.0954 7.49968L13.7109 6.41988V8.57948Z" />
  </SvgIcon>
);

export const InfoIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox="0 0 10 10" {...props}>
    <path d="M4.49992 0.833374C2.19992 0.833374 0.333252 2.70004 0.333252 5.00004C0.333252 7.30004 2.19992 9.16671 4.49992 9.16671C6.79992 9.16671 8.66659 7.30004 8.66659 5.00004C8.66659 2.70004 6.79992 0.833374 4.49992 0.833374ZM4.91659 7.08337H4.08325V4.58337H4.91659V7.08337ZM4.91659 3.75004H4.08325V2.91671H4.91659V3.75004Z" />
  </SvgIcon>
);

export const FolderIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox={"0 0 16 16"} {...props}>
    <path
      d="M5.65625 0.65625L7 2H12.3438C12.6979 2 13 2.13542 13.25 2.40625C13.5208 2.67708 13.6562 2.98958 13.6562 3.34375V10C13.6562 10.3542 13.5208 10.6667 13.25 10.9375C13 11.2083 12.6979 11.3438 12.3438 11.3438H1.65625C1.30208 11.3438 0.989583 11.2083 0.71875 10.9375C0.46875 10.6667 0.34375 10.3542 0.34375 10V2C0.34375 1.64583 0.46875 1.33333 0.71875 1.0625C0.989583 0.791667 1.30208 0.65625 1.65625 0.65625H5.65625Z"
      fill="white"
    />
  </SvgIcon>
);

export const LoadingIcon = (props: SvgIconProps) => (
  <SvgIcon viewBox={"0 0 16 16"} {...props}>
    <path
      d="M8.46094 8.46094L8.92578 7.69531L6.30078 6.10938V3.07422H5.42578V6.57422L8.46094 8.46094ZM1.87109 1.89844C3.01953 0.75 4.39583 0.175781 6 0.175781C7.60417 0.175781 8.97135 0.75 10.1016 1.89844C11.25 3.02865 11.8242 4.39583 11.8242 6C11.8242 7.60417 11.25 8.98047 10.1016 10.1289C8.97135 11.2591 7.60417 11.8242 6 11.8242C4.39583 11.8242 3.01953 11.2591 1.87109 10.1289C0.740885 8.98047 0.175781 7.60417 0.175781 6C0.175781 4.39583 0.740885 3.02865 1.87109 1.89844Z"
      fill="white"
    />
  </SvgIcon>
);

export const ArrowRight = (props: SvgIconProps) => (
  <SvgIcon viewBox={"0 0 7 11"} {...props}>
    <path d="M6.76154 6.08419L2.15332 10.7577C1.83482 11.0808 1.31978 11.0808 1.00466 10.7577L0.238882 9.9811C-0.0796273 9.65808 -0.0796273 9.13574 0.238882 8.81615L3.50529 5.50344L0.238882 2.19072C-0.0796273 1.8677 -0.0796273 1.34536 0.238882 1.02577L1.00127 0.242268C1.31978 -0.080756 1.83482 -0.080756 2.14994 0.242268L6.75815 4.91581C7.08005 5.23883 7.08005 5.76117 6.76154 6.08419Z" />
  </SvgIcon>
);

export const ArrowLeft = (props: SvgIconProps) => (
  <SvgIcon viewBox={"0 0 7 11"} {...props}>
    <path d="M0.238461 4.91581L4.84668 0.242269C5.16518 -0.0807552 5.68022 -0.0807552 5.99534 0.242269L6.76112 1.0189C7.07963 1.34192 7.07963 1.86426 6.76112 2.18385L3.49471 5.49656L6.76112 8.80928C7.07963 9.1323 7.07963 9.65464 6.76112 9.97423L5.99873 10.7577C5.68022 11.0808 5.16518 11.0808 4.85006 10.7577L0.241849 6.08419C-0.0800486 5.76117 -0.0800486 5.23883 0.238461 4.91581Z" />
  </SvgIcon>
);
