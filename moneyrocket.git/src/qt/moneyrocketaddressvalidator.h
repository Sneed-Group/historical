// Copyright (c) 2011-2020 The Moneyrocket Core developers
// Distributed under the MIT software license, see the accompanying
// file COPYING or http://www.opensource.org/licenses/mit-license.php.

#ifndef MONEYROCKET_QT_MONEYROCKETADDRESSVALIDATOR_H
#define MONEYROCKET_QT_MONEYROCKETADDRESSVALIDATOR_H

#include <QValidator>

/** Base58 entry widget validator, checks for valid characters and
 * removes some whitespace.
 */
class MoneyrocketAddressEntryValidator : public QValidator
{
    Q_OBJECT

public:
    explicit MoneyrocketAddressEntryValidator(QObject *parent);

    State validate(QString &input, int &pos) const override;
};

/** Moneyrocket address widget validator, checks for a valid moneyrocket address.
 */
class MoneyrocketAddressCheckValidator : public QValidator
{
    Q_OBJECT

public:
    explicit MoneyrocketAddressCheckValidator(QObject *parent);

    State validate(QString &input, int &pos) const override;
};

#endif // MONEYROCKET_QT_MONEYROCKETADDRESSVALIDATOR_H
