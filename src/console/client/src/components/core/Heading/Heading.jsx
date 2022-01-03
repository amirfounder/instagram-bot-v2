import React from 'react';
import styles from './Heading.module.scss';

export const Heading = (props) => {
  const {
    level,
    children,
    className,
    ignoreMargin,
    ...other
  } = props;

  const finalClassName = `
    ${styles.main}
    ${className}
    ${!ignoreMargin && styles.margin}
  `;

  return (
    <>
      {
        Number(level) === 1 ? <h1 data-testid='heading-1' {...other} className={finalClassName}>{children}</h1> :
        Number(level) === 2 ? <h2 data-testid='heading-2' {...other} className={finalClassName}>{children}</h2> :
        Number(level) === 3 ? <h3 data-testid='heading-3' {...other} className={finalClassName}>{children}</h3> :
        Number(level) === 4 ? <h4 data-testid='heading-4' {...other} className={finalClassName}>{children}</h4> :
        Number(level) === 5 ? <h5 data-testid='heading-5' {...other} className={finalClassName}>{children}</h5> :
        Number(level) === 6 ? <h6 data-testid='heading-6' {...other} className={finalClassName}>{children}</h6> :
        <h2 data-testid='heading-2' {...other} className={finalClassName}>{children}</h2>
      }
    </>
  )
}