import sys, os, time
from datetime import datetime
from timeit import default_timer as timer
try:
    from humanfriendly import format_timespan
except ImportError:
    def format_timespan(seconds):
        return "{:.2f} seconds".format(seconds)

import logging
logging.basicConfig(format='%(asctime)s %(name)s.%(lineno)d %(levelname)s : %(message)s',
        datefmt="%H:%M:%S",
        level=logging.INFO)
# logger = logging.getLogger(__name__)
logger = logging.getLogger('__main__').getChild(__name__)

# from logging.handlers import SMTPHandler
# from smtp_args import SMTP_ARGS, email_logger
# email_handler = SMTPHandler(**SMTP_ARGS)
# email_logger = logging.getLogger('email_logger')
# email_logger.addHandler(email_handler)
# email_logger.setLevel = logging.INFO

def raiseerr():
    raise RuntimeError("raising a test error")

def main(args):
    # raiseerr()
    if email_logger:
        some_var = 'data'
        EMAIL_LOG.append("logging some info: {}".format(some_var))

if __name__ == "__main__":
    total_start = timer()
    logger = logging.getLogger(__name__)
    PROGRAM_ARGS = " ".join(sys.argv)
    logger.info(PROGRAM_ARGS)
    logger.info( '{:%Y-%m-%d %H:%M:%S}'.format(datetime.now()) )
    import argparse
    parser = argparse.ArgumentParser(description="smtp logger")
    parser.add_argument("--debug", action='store_true', help="output debugging info")
    parser.add_argument("--email", action='store_true', help="send email notifications")
    global args
    args = parser.parse_args()
    if args.debug:
        logger.setLevel(logging.DEBUG)
        logger.debug('debug mode is on')
    else:
        logger.setLevel(logging.INFO)
    if args.email:
        try:
            from email_logger import email_logger
            # email_logger.propagate = False
        except ImportError:
            logger.error("failed to load email_logger")
            email_logger = None
            args.email = False
        except RuntimeError as e:
            logger.error(e)
            email_logger = None
            args.email = False
        if email_logger:
            logger.info("email notifications are on")
            def email_exc(exctype, value, tb):
                from traceback import format_exception
                out = ""
                if EMAIL_LOG:
                    out = out + "\n".join(EMAIL_LOG)
                    out = out + "\n"
                out = "EXCEPTION ENCOUNTERED\n\n"
                out = out + "".join(format_exception(exctype, value, tb))
                email_logger.error(out)
                sys.__excepthook__(exctype, value, tb)  # normal exception behavior
            sys.excepthook = email_exc
        EMAIL_LOG = [PROGRAM_ARGS]
    else:
        email_logger = None
    main(args)
    total_end = timer()
    final_time_str = 'all finished. total time: {}'.format(format_timespan(total_end-total_start))
    # logger.info('all finished. total time: {}'.format(format_timespan(total_end-total_start)))
    logger.info(final_time_str)
    if args.email:
        out = ""
        if EMAIL_LOG:
            out = out + "\n".join(EMAIL_LOG)
            out = out + "\n\n"
        out = out + "PROGRAM FINISHED\n\n"
        out = out + final_time_str
        email_logger.info(out)
